#! /usr/bin/env bash

git clean -fxd && snakemake --cores && snakemake -s Snakefile.eval --cores

