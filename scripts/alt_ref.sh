#! /usr/bin/env bash

# required programs: tabix (samtools), bgzip (samtools), vcf-consensus (vcftools)

#set -x
set -euf -o pipefail

. _pipelinelib.sh

if [ $# -ne 4 ];
then
	help_message_exit \
		"${0##*/} reference.fa variants.vcf chainfile.chain new_fa.fa" \
		"Create a new FASTA file by incorporating variants.vcf into reference.fa and print it to the standard output."
fi

check_file $1
check_file $2

reference=$1
variantsOriginal=$2
variants=${variantsOriginal}.tmp.vcf 	# TMP file
cp $variantsOriginal $variants

bgzip $variants
gzfile=${variants}.gz

tabix $gzfile 
#cat $reference \
#	| vcf-consensus ${variants}.gz
../bin/bcftools consensus -f $reference -c $3 -o $4 ${variants}.gz
rm ${variants}.gz ${variants}.gz.tbi

