#! /usr/bin/env bash

# compute edit distances for a run

set -o pipefail
#set -x

if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters"
	exit 1
fi

cd $1
f="updates.tsv"
echo "" > $f


count=`for x in 2_alignments.itref/5_vcf/*.vcf.gz; do bcftools view $x; done | grep -v "#"| wc -l`
echo "itref_sum	$count" >> $f

count=`for x in 2_alignments.dyn/5_vcf/*.vcf.gz; do bcftools view $x; done | grep -v "#"| wc -l`
echo "dyn_sum	$count" >> $f

for m in dyn itref; do
	echo >> $f
	for x in 2_alignments.${m}/5_vcf/*.vcf.gz; do
		upd=`bcftools view $x | grep -v "#"| wc -l`
		b=`basename $x`
		echo "$x	$upd" >> $f
	done
done


echo >> $f
