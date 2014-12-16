import os,sys

configfile: "conf.json"

###################
## METHODS ##
###################

DYNAMIC="stat"
STATIC="dyn"

###################
## CONFIGURATION ##
###################

DEBUG = False

include: "inc_filenames.py"
include: "inc_proc.py"

ruleorder:
    init > consensus

shell.prefix(" set -euf -o pipefail; ")

###################
## PROGRAM NAMES ##
###################

MAPREADS        = "scripts/map_reads.sh"
BWA             = "bin/bwa"
BCFTOOLS        = "bin/bcftools"
DWGSIM          = "bin/dwgsim"
SAMTOOLS        = "bin/samtools"
TABIX           = "bin/tabix"
BGZIP           = "bin/bgzip"
CALLVARIANTS    = "bin/call_variants"

#
# BASIC RULES
#

rule all:
    input:
        #bam_file(STATIC,50)
        #"experiment/bwa-mem/s/bam/experiment.bwa-mem.s_0001.bam",
        #report_file()
        bam_file(STATIC, int(config["S_number_of_iterations"])),
        bam_file(DYNAMIC, int(config["_DU_number_of_iterations"])),

rule static:
    input:
        bam_file(STATIC, int(config["S_number_of_iterations"])),

rule dynamic:
    input:
        bam_file(DYNAMIC, int(config["_DU_number_of_iterations"])),

#
# SHARED RULES
#

rule init:
    input:
        config["G_reference"]
    output:
        fa_file("{method}",0)
    message:
        message("D - init " + config["G_reference"])
    shell:
        "cp {input[0]} {output[0]}"

def f_call_variants(wildcards):
    cur_it=int(str(wildcards.iteration))
    if cur_it==0:
        return []
    else:
        return [
            fa_file(wildcards.method, cur_it -1),
            bam_file(wildcards.method, cur_it -1)
        ]

rule call_variants:
    input:
        f_call_variants,
        SAMTOOLS,
        CALLVARIANTS,
    output:
        vcf_file("{method}","{iteration}")
    message:
        message("D - calling variants")
    params:
        SAMTOOLS=SAMTOOLS,
        CALLVARIANTS=CALLVARIANTS,
    run:
        shell("""{params.SAMTOOLS} mpileup\
                        --min-MQ 0 \
                        {input[1]} | \
                {params.CALLVARIANTS}\
                        --calling-alg parikh \
                        --reference {input[0]} \
                        --min-coverage 2 \
                        --min-base-qual 0 \
                        --accept-level 0.6 \
                        > {output[0]}""")

def f_consensus(wildcards):
    cur_it=int(str(wildcards.iteration))
    if int(str(wildcards.iteration))==0:
        return []
    else:
        return fa_file(wildcards.method, cur_it -1),

rule consensus:
    input:
        f_consensus,
        vcf_c_file("{method}","{iteration}"),
        vcf_c_i_file("{method}","{iteration}"),
        BCFTOOLS,
    output:
        fa_file("{method}","{iteration}"),
        chain_file("{method}","{iteration}"),
    params:
        BCFTOOLS=BCFTOOLS
    shell:
        """{params.BCFTOOLS} consensus \
            -f {input[0]}\
            -c {output[1]} \
            {input[1]} \
            > {output[0]}
        """

#
# DYNAMIC MAPPING
#

rule d_map_reads:
    output:
        bam_file(DYNAMIC,"{iteration}")
    input:
        BWA,
        SAMTOOLS,
        fa_file(DYNAMIC,"{iteration}"),
        fq_file(),
        MAPREADS
    params:
        output_prefix=bam_file(DYNAMIC,"{iteration}")[:-4],
        MAPREADS=MAPREADS,
        mapper=config["G_mapper"],
        fq=fq_file(),
    message:
        message("D - mapping reads")
    run:
        faf=fa_file(DYNAMIC,int(wildcards.iteration))
        ln_start= int(wildcards.iteration) * 4 * config["_DU_reads_per_iteration"] + 1
        ln_end= int(ln_start) + 4 * config['_DU_reads_per_iteration']  - 1

        shell("""
            {{params.MAPREADS}}\
                {{params.mapper}}\
                {fa}\
                <(sed -n 1,{ln_end}p {{params.fq}})\
                {{params.output_prefix}}
        """.format(
            fa=faf,
            ln_start=ln_start,
            ln_end=ln_end
        ))

#
# STATIC MAPPING
#

rule s_map_reads:
    output:
        bam_file(STATIC, "{iteration}")
    input:
        fa_file(STATIC, "{iteration}"),
        fq_file(),
        BWA,
        SAMTOOLS,
        BGZIP,
        TABIX,
        MAPREADS
    params:
        output_prefix=bam_file(STATIC, "{iteration}")[:-4],
        MAPREADS=MAPREADS,
        mapper=config["G_mapper"],
    log:
        "test.txt"
    message:
        message("S - mapping reads")
    shell:
        "{params.MAPREADS} {params.mapper} {input[0]} {input[1]} {params.output_prefix}"

#
# OTHER
#
        
rule simulate_reads:
    input:
        DWGSIM,
        config["G_reference"]
    output:
        fq_file(),
        temp(fq_file()+".bwa.read1.fastq"),
        temp(fq_file()+".bwa.read2.fastq"),
        temp(fq_file()+".mutations.txt"),
    message:
        message("Simulating reads")
    params:
        error_rate=str(config['R_error_rate']),
        number_of_reads=str(config["_G_number_of_reads"]),
        read_length=str(config["R_read_length"]),
        rate_of_mutations=str(config["R_rate_of_mutations"]),
        fraction_of_indels=str(config["R_fraction_of_indels"]),
        reference=config["G_reference"],
        fq=fq_file()
    shell:
        """
            dwgsim \
                -e {params.error_rate} \
                -N {params.number_of_reads} \
                -1 {params.read_length} \
                -2 0 \
                -r {params.rate_of_mutations} \
                -R {params.fraction_of_indels} \
                -z 1 \
                {params.reference} \
                {params.fq}
                
                mv {params.fq}.bfast.fastq {params.fq}
        """

rule vcf_compress:
    input:
        "{vcffile}.vcf",
        BGZIP
    output:
        "{vcffile}.vcf.gz"
    params:
        BGZIP=BGZIP
    shell:
        """{params.BGZIP} \
            {input[0]} \
            -c > {output[0]}
        """

rule vcf_index:
    input:
        "{vcffile}.vcf.gz",
        TABIX
    output:
        "{vcffile}.vcf.gz.tbi"
    params:
        TABIX=TABIX
    shell:
        """{params.TABIX} {input[0]}"""
#
# REPORTS
#

rule reports:
    input:
        bam_file(DYNAMIC, int(config["_DU_number_of_iterations"])),
        bam_file(STATIC, int(config["S_number_of_iterations"])),
        config_file()
    output:
        report_file()
    params:
        i1=os.path.dirname(bam_file(DYNAMIC, 0)),
        i2=os.path.dirname(bam_file(STATIC, 0)),
        o=report_file(),
        c=config_file()
    shell:
        "lavender_report.py -i {params.i1} {params.i2} -o {params.o} -c {params.c}"
    
rule conf:
    output:
        config_file()
    run:
        with open(config_file(),"w+") as f:
            for x in config.keys():
                print("{}={}".format(x,repr(config[x]).replace("'","\"")),file=f)
    


#
# PROGRAMS
#

rule prog_dwgsim:
    message:
        "Compiling DwgSim"
    output:
        DWGSIM
    shell:
        """
            cd src_ext
            cd dwgsim
            git submodule init
            git submodule update
            make
            cd ..
            cd ..
            cp src_ext/dwgsim/dwgsim {output[0]}
        """

rule prog_samtools:
    message:
        "Compiling SamTools"
    output:
        SAMTOOLS
    shell:
        """
            cd src_ext
            cd samtools
            make
            cd ..
            cd ..
            cp src_ext/samtools/samtools {output[0]}
        """

rule prog_htslib:
    message:
        "Compiling HtsLib"
    output:
        TABIX,
        BGZIP
    shell:
        """
            cd src_ext
            cd htslib
            make
            cd ..
            cd ..
            cp src_ext/htslib/tabix {output[0]}
            cp src_ext/htslib/bgzip {output[1]}
        """

rule prog_bcftools:
    message:
        "Compiling BcfTools"
    output:
        BCFTOOLS
    shell:
        """
            cd src_ext
            cd bcftools
            make
            cd ..
            cd ..
            cp src_ext/bcftools/bcftools {output[0]}
        """


# BWA

rule prog_bwa:
    message:
        "Compiling BWA "
    output:
        BWA
    run:
        shell("""
            cd src_ext
            cd bwa
            make
            cd ..
            cd ..
            cp src_ext/bwa/bwa {output[0]}
        """)

# CALL VARIANTS

rule prog_call_variants:
    message:
        "Compiling CallVariants "
    output:
        CALLVARIANTS
    run:
        shell("""
            cd call_variants
            cmake .
            make
            cd ..
            cp call_variants/call_variants {output[0]}
        """)



# LAVEnder

#
# DATA
#

rule data_reference:
    output:
        config["G_reference"]
    run:
        shell("curl --insecure -o {output[0]} {config[G_reference_address]}")




