import os,sys

configfile: "conf.json"

include: "inc_filenames.py"
include: "inc_proc.py"

ruleorder: s_init > s_call_variants
ruleorder: d_init > d_call_variants

shell.prefix(" set -euf -o pipefail; ")

#d_output_file = ".d.tmp"
#s_output_file = ".s.tmp"


###################
## PROGRAM NAMES ##
###################

DWGSIM          = "bin/dwgsim"
SAMTOOLS        = "bin/samtools"
TABIX           = "bin/tabix"
BGZIP           = "bin/bgzip"


#
# BASIC RULES
#

rule all:
	input: report_file()

rule static:
	run:
		pass

rule dynamic:
	run:
		pass



#
# DYNAMIC MAPPING
#

rule d_init:
	input:
		config["G_reference"]
	output:
		d_fa(0)
	message:
		message("D - init "+config["G_reference"])
	shell:
		"cp {} {}".format(
			config["G_reference"],
			d_fa(0)
		)


rule d_call_variants:
	input:
		lambda wildcards: [] if int(str(wildcards.iteration))==0 else [
			d_fa( int(str(wildcards.iteration)) -1 ),
			d_bam( int(str(wildcards.iteration)) -1 )
		]		
	output:
		d_fa("{iteration}"),
		d_vcf("{iteration}")
	message:
		message("S - calling variants")
	shell:
		"""(samtools mpileup\
                        --min-MQ 0 \
                        {input[1]} | \
                call_variants\
                        --calling-alg parikh \
                        --reference {input[0]} \
                        --min-coverage 2 \
                        --min-base-qual 0 \
                        --accept-level 0.6 \
			--vcf {output[1]} \
		 \
                > {output[0]}) """

rule d_map_reads:
	output:
		d_bam("{iteration}")
	input:
		d_fa("{iteration}"),
		fq_file()
	params:
		output_prefix=d_bam("{iteration}")[:-4],
	message:
		message("D - mapping reads")
	run:
		ln_start=int(wildcards.iteration) * 4 * config["_DU_reads_per_iteration"] + 1
		ln_end=ln_start + 4 * config['_DU_reads_per_iteration']  - 1
		shell("map_reads.sh {mapper} {fa} <(sed -n 1,{ln_end}p {fq}) {output_prefix}".format(
			mapper="bwa-mem",
			fa=d_fa(int(wildcards.iteration)),
			ln_end=ln_end,
			fq=fq_file(),
			output_prefix=d_bam(int(wildcards.iteration))[:-4]
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
		message("S - init "+config["G_reference"])
	shell:
		"cp {} {}".format(
			config["G_reference"],
			s_fa(0)
		)


rule s_call_variants:
	input:
		lambda wildcards: [] if int(str(wildcards.iteration))==0 else [
			s_fa( int(str(wildcards.iteration)) -1 ),
			s_bam( int(str(wildcards.iteration)) -1 )
		]		
	output:
		s_fa("{iteration}"),
		s_vcf("{iteration}")
	message:
		message("S - calling variants")
	shell:
		"""samtools mpileup\
                        --min-MQ 0 \
                        {input[1]} | \
                call_variants\
                        --calling-alg parikh \
                        --reference {input[0]} \
                        --min-coverage 2 \
                        --min-base-qual 0 \
                        --accept-level 0.6 \
			--vcf {output[1]} \
                > {output[0]} """

rule s_map_reads:
	output:
		s_bam("{iteration}")
	input:
		s_fa("{iteration}"),
		fq_file()
	params:
		output_prefix=s_bam("{iteration}")[:-4]
	log:
		"test.txt"
	message:
		message("S - mapping reads")
	shell:
		"map_reads.sh bwa-mem {input[0]} {input[1]} {params.output_prefix}"

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
	shell:
		"""
			dwgsim \
				-e {error_rate} \
				-N {number_of_reads} \
				-1 {read_length} \
				-2 0 \
				-r {rate_of_mutations} \
				-R {fraction_of_indels} \
				-z 1 \
				{reference} \
				{fq}
                
				mv {fq}.bfast.fastq {fq}
		""".format(
			error_rate=config['R_error_rate'],
			number_of_reads=config["_G_number_of_reads"],
			read_length=config["R_read_length"],
			rate_of_mutations=config["R_rate_of_mutations"],
			fraction_of_indels=config["R_fraction_of_indels"],
			reference=config["G_reference"],
			fq=fq_file()
		)


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
	shell:
		"lavender_report.py -i {i1} {i2} -o {o} -c {c}".format(
			i1=os.path.dirname(d_bam(0)),
			i2=os.path.dirname(s_bam(0)),
			o=report_file(),
			c=config_file()

		)
	
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


# SAMTOOLS

# DWGSIM


rule prog_dwgsim:
	message:
		"Compiling DwgSim"
	output:
		DWGSIM
	shell:
		"""
			cd DWGSIM
			git submodule init
			git submodule update
			make
			cp dwgsim {DWGSIM}
			cd ..
		""".format(
			DWGSIM=os.path.join("..",DWGSIM)
		)

rule prog_samtools:
	message:
		"Compiling SamTools"
	output:
		SAMTOOLS
	shell:
		"""
			cd samtools
			make
			cp samtools {SAMTOOLS}
			cd ..
		""".format(
			SAMTOOLS=os.path.join("..",SAMTOOLS)
		)

rule prog_htslib:
	message:
		"Compiling HtsLib"
	output:
		TABIX,
		BGZIP
	shell:
		"""
			cd htslib
			make
			cp tabix {TABIX}
			cp bgzip {BGZIP}
			cd ..
		""".format(
			TABIX=os.path.join("..",TABIX),
			BGZIP=os.path.join("..",BGZIP)
		)


# LAVEnder

#
# DATA
#

rule data_reference:
	output:
		config["G_reference"]
	run:
		shell("curl --insecure -o {} {}".format(
			config["G_reference"],
			config["G_reference_address"],
		))




