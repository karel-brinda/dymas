import os,sys

configfile: "conf.json"

include: "inc_filenames.py"
include: "inc_proc.py"

ruleorder: s_init > s_call_variants
ruleorder: d_init > d_call_variants

shell.prefix(" set -euf -o pipefail; ")

#shell("git submodule init")
#shell("git submodule update")


#d_output_file = ".d.tmp"
#s_output_file = ".s.tmp"


###################
## PROGRAM NAMES ##
###################

ALTREF          = "scripts/alt_ref.sh"
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
        report_file()

rule static:
    input:
        s_bam(int(config["S_number_of_iterations"])),

rule dynamic:
    input:
        d_bam(int(config["_DU_number_of_iterations"])),



#
# DYNAMIC MAPPING
#

rule d_init:
    input:
        config["G_reference"]
    output:
        d_fa(0)
    message:
        message("D - init " + config["G_reference"])
    shell:
        "cp {input[0]} {output[0]}"

rule d_call_variants:
    input:
        lambda wildcards: [] if int(str(wildcards.iteration))==0 else [
            d_fa( int(str(wildcards.iteration)) -1 ),
            d_bam( int(str(wildcards.iteration)) -1 )
        ],
        SAMTOOLS,
        CALLVARIANTS,
        ALTREF,
        BCFTOOLS
    output:
        d_fa("{iteration}"),
        d_chain("{iteration}"),
        d_vcf("{iteration}")
    message:
        message("S - calling variants")
    params:
        ALTREF=ALTREF,
        SAMTOOLS=SAMTOOLS,
        CALLVARIANTS=CALLVARIANTS
    shell:
        """{params.SAMTOOLS} mpileup\
                        --min-MQ 0 \
                        {input[1]} | \
                {params.CALLVARIANTS}\
                        --calling-alg parikh \
                        --reference {input[0]} \
                        --min-coverage 2 \
                        --min-base-qual 0 \
                        --accept-level 0.6 \
                        --vcf {output[1]} \
                > /dev/null """

        """{params.ALTREF} \
            {input[0]} \
            {output[1]} \
            {output[2]} \
            {output[0]}
        """

rule d_map_reads:
    output:
        d_bam("{iteration}")
    input:
        BWA,
        SAMTOOLS,
        d_fa("{iteration}"),
        fq_file(),
        MAPREADS
    params:
        output_prefix=d_bam("{iteration}")[:-4],
        MAPREADS=MAPREADS,
        mapper="bwa-mem",
        fq=fq_file(),
        #output_prefix=d_bam(int(wildcards.iteration))[:-4]

    message:
        message("D - mapping reads")
    run:
        fa=d_fa(int(wildcards.iteration))
        ln_start= int(wildcards.iteration) * 4 * config["_DU_reads_per_iteration"] + 1
        ln_end= int(ln_start) + 4 * config['_DU_reads_per_iteration']  - 1

        shell("""
            {{params.MAPREADS}}\
                {{params.mapper}}\
                {fa}\
                <(sed -n 1,{ln_end}p {{params.fq}})\
                {{params.output_prefix}}
        """.format(
            fa=fa,
            ln_start=ln_start,
            ln_end=ln_end
        ))

#
# STATIC MAPPING
#

rule s_init:
    input:
        config["G_reference"]
    output:
        s_fa(0)
    message:
        message("S - init " + config["G_reference"])
    shell:
        """cp {config[G_reference]} {output[0]}"""


rule s_call_variants:
    input:
        lambda wildcards: [] if int(str(wildcards.iteration))==0 else [
            s_fa( int(str(wildcards.iteration)) -1 ),
            s_bam( int(str(wildcards.iteration)) -1 )
        ],
        SAMTOOLS,
        CALLVARIANTS,
        ALTREF,
        BCFTOOLS
    output:
        s_fa("{iteration}"),
        s_vcf("{iteration}"),
        s_chain("{iteration}")
    message:
        message("S - calling variants")
    params:
        ALTREF=ALTREF,
        CALLVARIANTS=CALLVARIANTS,
        SAMTOOLS=SAMTOOLS
    shell:
        """{params.SAMTOOLS} mpileup\
                        --min-MQ 0 \
                        {input[1]} | \
                {params.CALLVARIANTS}\
                        --calling-alg parikh \
                        --reference {input[0]} \
                        --min-coverage 2 \
                        --min-base-qual 0 \
                        --accept-level 0.6 \
                        --vcf {output[1]} \
                > /dev/null """

        """{params.ALTREF} \
            {input[0]} \
            {output[1]} \
            {output[2]} \
            {output[0]}
        """

#       """{params.SAMTOOLS} mpileup\
#                        --min-MQ 0 \
#                        {input[1]} | \
#                {params.CALLVARIANTS}\
#                        --calling-alg parikh \
#                        --reference {input[0]} \
#                        --min-coverage 2 \
#                        --min-base-qual 0 \
#                        --accept-level 0.6 \
#                       --vcf {output[1]} \
#                > {output[0]} """

rule s_map_reads:
    output:
        s_bam("{iteration}")
    input:
        s_fa("{iteration}"),
        fq_file(),
        BWA,
        SAMTOOLS,
        MAPREADS
    params:
        output_prefix=s_bam("{iteration}")[:-4],
        MAPREADS=MAPREADS
    log:
        "test.txt"
    message:
        message("S - mapping reads")
    shell:
        "{params.MAPREADS} bwa-mem {input[0]} {input[1]} {params.output_prefix}"

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


#
# REPORTS
#

rule reports:
    input:
        d_bam(int(config["_DU_number_of_iterations"])),
        s_bam(int(config["S_number_of_iterations"])),
        config_file()
    output:
        report_file()
    params:
        i1=os.path.dirname(d_bam(0)),
        i2=os.path.dirname(s_bam(0)),
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




