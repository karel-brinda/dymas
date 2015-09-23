#! /usr/bin/env bash

set -e

for snakefile in `ls Snakefile.*`; do
	snakemake -s $snakefile --cores
done

