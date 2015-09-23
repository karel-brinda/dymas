#! /usr/bin/env bash

set -e

snakemake -s Snakefile.1_reads --cores
snakemake -s Snakefile.2_exp --cores
snakemake -s Snakefile.3_eval --cores

