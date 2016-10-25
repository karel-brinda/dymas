#! /usr/bin/env bash

set -x

cd "$(dirname "$0")"

mkdir -p ~/.smbl/bin
cp smbl_executor.sh ~/.smbl/bin
cp gnuplot5 ~/.smbl/bin

cd ~/.smbl/bin

progs="bwa samtools bcftools dwgsim bowtie2"

for x in $progs; do
	echo linking $x
	rm -f $x
	ln -s smbl_executor.sh $x
done;

