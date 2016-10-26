#! /usr/bin/env bash

# obtain species reference for a run
# can be run when experiment is finished

set -o pipefail
set -x

if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters"
	exit 1
fi

cd $1/1_reads/001/

if [ -e "dwgsim_files.pe.1.mutations.vcf.gz" ]; then
	(>&2 echo "vcf.gz already exists")
else
	bgzip dwgsim_files.pe.1.mutations.vcf
	tabix dwgsim_files.pe.1.mutations.vcf.gz
fi

bcftools consensus -i -f ../../2_alignments.itref/1_reference/00000.fa dwgsim_files.pe.1.mutations.vcf.gz

