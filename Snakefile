import os,sys

configfile: "conf.json"

ruleorder: s_init > s_call_variants
ruleorder: d_init > d_call_variants

shell.prefix(" set -euf -o pipefail; ")

#d_output_file = ".d.tmp"
#s_output_file = ".s.tmp"



#
# CONFIGURATION TEST
#


def message(x):
	return """
	==========================================================================================
	{x}
		input:	{{input}}
		output:	{{output}}
	==========================================================================================
	
	""".format(x=x)
		
def format_nb(x):
	return str(x).zfill(4) if isinstance(x,int) else x
	
def fq_file():
	return os.path.join(config["G_experiment_name"],"reads","{}__{}_{}_{}.fq".format(
		config["G_reference"],
		config["R_read_length"],
		config["R_rate_of_mutations"],
		config["R_error_rate"] ) 
	)

def config_file():
	return ".{}.conf".format(
			config["G_experiment_name"],
		)
	
def report_file():
	return "report__{}__{}".format(
				config["G_experiment_name"],
				config["G_mapper"]
			)
	
	
rule all:
	input: report_file()


	#
# DYNAMIC MAPPING
#



def d_prefix():
	return os.path.join(config["G_experiment_name"],config["G_mapper"],"dynamic")

def d_bam(it):
	return os.path.join(d_prefix(),"bam","{}.{}.d_{}.bam".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

def d_fa(it):
	return os.path.join(d_prefix(),"fa","{}.{}.d_{}.fa".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

def d_vcf(it):
	return os.path.join(d_prefix(),"vcf","{}.{}.d_{}.vcf".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

rule d_init:
	input:
		config["G_reference"]
	output:
		d_fa(0)
	message:
		message("D - init "+config["G_reference"])
	shell:
		"cp bact.fasta {}".format(d_fa(0))


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
	benchmark:
		"test.json"
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

def s_prefix():
	return os.path.join(config["G_experiment_name"],config["G_mapper"],"static")

def s_bam(it):
	return os.path.join(s_prefix(),"bam","{}.{}.s_{}.bam".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

def s_fa(it):
	return os.path.join(s_prefix(),"fa","{}.{}.s_{}.fa".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

def s_vcf(it):
	return os.path.join(s_prefix(),"vcf","{}.{}.s_{}.vcf".format(config["G_experiment_name"],config["G_mapper"],format_nb(it)) )

#rule s_all:
#	input:
#		s_bam(int(config["S_number_of_iterations"]))
#	output:
#		s_output_file
#	shell:
#		"touch "+s_output_file

	
rule s_init:
	input:
		config["G_reference"]
	output:
		s_fa(0)
	message:
		message("S - init "+config["G_reference"])
	shell:
		"cp bact.fasta {}".format(s_fa(0))


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
	
