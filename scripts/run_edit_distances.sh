#! /usr/bin/env bash

# compute edit distances for a run

set -o pipefail
#set -x

if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters"
	exit 1
fi

d=`dirname $0`
ref="$d/run_dwgsim_ref.sh"

spec=1_reads/individual.fa

cd $1
$ref ./ > $spec

for m in dyn itref; do
	f="edit_dist_${m}.tsv"
	echo > $f
	for x in 2_alignments.${m}/1_reference/*.fa; do
		dist=`aligner $spec $x | grep "#" | awk '{print $2}'`
		b=`basename $x`
		echo "$x	$b	$dist" >> $f
	done
done

