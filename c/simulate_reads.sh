#! /usr/bin/env bash

#set -x
set -euf -o pipefail

. _pipelinelib.sh

if [ $# -ne 1 ];
then
	help_message_exit \
		"${0##*/} config.conf" \
		"" 
fi

check_file $1
config=$1
. _load_config.sh $config
tmp_prefix="${G_experiment_name}.tmp_reads"

# only unless reads are already generated
if [ ! -f $G_reads ] || [ $experiment_configuration -nt $G_reads ] 
then

	dwgsim \
		-e $R_error_rate \
		-N $_G_number_of_reads \
		-1 $R_read_length \
		-2 0 \
		-r $R_rate_of_mutations \
		-R $R_fraction_of_indels \
		-X $R_prob_indel_extended \
		-I $R_minimum_length_of_indel \
		-y $R_prob_random_read \
		-z 1 \
		$G_reference \
		$tmp_prefix
		
	mv ${tmp_prefix}.bfast.fastq $G_reads
	create_alternative_reference.sh $G_reference ${tmp_prefix}.mutations.vcf > $R_alternative_reference 2> /dev/null
	rm -f ${tmp_prefix}.bwa.read1.fastq
	rm -f ${tmp_prefix}.bwa.read2.fastq
	rm -f ${tmp_prefix}.mutations.txt
fi
