#! /usr/bin/env bash

set -e

for snakefile in `ls Snakefile.*`; do
	echo
	echo "-------------"
	echo "$snakefile"
	echo "-------------"
	echo
	snakemake -s $snakefile --cores -p
done

