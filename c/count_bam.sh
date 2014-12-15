#! /usr/bin/env bash

#set -x
set -euf -o pipefail

. _pipelinelib.sh

if [ $# -ne 2 ];
then
	if [ $# -ne 1 ];
	then
		help_message_exit \
			"${0##*/} alignment.bam [what_to_count]" \
			"what_to_count:
	reads                   - total number of alignments
	mapped_reads            - number of mapped reads (without flag 4)
	unmapped_reads          - number of unmapped reads (with flag 4)
	all                     - all of previous (default)"
	else
		what=all
	fi

else
	what=$2
fi

bamfile=$1

check_file $bamfile

function reads {
	#samtools view $bamfile | cut -f1 | sort | uniq | wc -l
	samtools view -c $1
}

function mapped_reads {
	#samtools view -F 4 $bamfile | cut -f1 | sort | uniq | wc -l
	samtools view -c -F 4 $1
}

function unmapped_reads {
	#samtools view -f 4 $bamfile | cut -f1 | sort | uniq | wc -l
	samtools view -c -f 4 $1
}

case "$what" in
	# since we use wgsim_eval.pl unique, samtools view -c suffices
	reads)
		reads $bamfile
		exit 0
		;;
         
	mapped_reads)
		mapped_reads $bamfile
		exit 0
		;;
         
	unmapped_reads)
		unmapped_reads $bamfile
		exit 0
		;;


	all)
		echo -n "reads:                       "
		reads $bamfile
		echo -n "mapped reads:                "
		mapped_reads $bamfile
		echo -n "unmapped reads:              "
		unmapped_reads $bamfile
		echo
		exit 0
		;;

	*)
		error_message_exit "Unknown value what_to_count: '$what'."
		;;
esac

