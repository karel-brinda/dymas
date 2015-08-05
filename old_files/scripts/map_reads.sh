#! /usr/bin/env bash

# when called in the pipeline: number of iteration must be included in prefix

set -x
set -ef -o pipefail
#set -v

#trap 'printf %s\\n "$BASH_COMMAND" >&2' DEBUG


. _pipelinelib.sh

set +u

dn=`dirname $0`
dn="${dn}/../bin"


#number_of_threads
if [ -n "$G_number_of_threads" ];
then
	number_of_threads=$G_number_of_threads
else
	number_of_threads=7
fi

set -u

if [ $# -ne 4 ];
then
	help_message_exit \
		"${0##*/} method reference.fa reads.fq output_prefix" \
		"	methods: bwa-aln / bwa-mem / bwa-sw / storm / gem / tigermap 
		
Map single-end reads to a reference genome. Technical info:
- Output files: output_prefix.sam, output_prefix.bam, output_prefix.bam.bai
- For every read only 1 alignment is kept (filtered by 'wgsim_eval.pl unique')."
	echo
fi

check_file $2
check_file $3

method=$1
reference=$2
reads=$3
prefix=$4

#
# MAPPING
#

case $method in
	bwa-aln)
		sai_file=$$.tmp.sai
		fq_file=$$.tmp.fq

		cat $reads > $fq_file

		#index
		~/.smbl/bin/bwa index $reference
		
		#mapping
		~/.smbl/bin/bwa aln -t $number_of_threads $reference $fq_file > $sai_file
		~/.smbl/bin/bwa samse $reference $sai_file $fq_file \
			| ~/.smbl/bin/samtools view -Shu - \
			| ~/.smbl/bin/samtools sort - $prefix
		rm $sai_file $fq_file
		rm ${reference}.amb ${reference}.ann ${reference}.bwt ${reference}.pac ${reference}.sa
		
		;;

	bwa-mem)
		#index
		~/.smbl/bin/bwa index $reference
		
		#mapping
		~/.smbl/bin/bwa mem -t $number_of_threads $reference $reads \
			| ~/.smbl/bin/samtools view -Shu - \
			| ~/.smbl/bin/samtools sort - $prefix
		rm ${reference}.amb ${reference}.ann ${reference}.bwt ${reference}.pac ${reference}.sa
		
		;;

	bwa-sw)
		#index
		~/.smbl/bin/bwa index $reference
		
		#mapping
		~/.smbl/bin/bwa bwasw -t $number_of_threads $reference $reads \
			| ~/.smbl/bin/samtools view -Shu - \
			| ~/.smbl/bin/samtools sort - $prefix
		rm ${reference}.amb ${reference}.ann ${reference}.bwt ${reference}.pac ${reference}.sa

		;;

	storm)
		#mapping
		tmp_pipe=${prefix}.tmp
		
		mkfifo $tmp_pipe
		storm-nucleotide -g $reference -r $reads -s "####-#--##-#--###-###" \
			| ${dn}/samtools view -Shu - \
			| ${dn}/samtools sort - $prefix
		;;

		#storm-nucleotide -g $reference -r $reads \
		#	| samtools view -Shu - \
		#	| samtools sort - $prefix
		#
		#;;
		
	gem)
		tmp_gem_index=${prefix}.gem.tmp
		tmp_gem_map=${prefix}.gem.tmp
	
		#index
		gem-indexer -T $number_of_threads -i $reference -o $tmp_gem_index   #2> /dev/null
	
		#mapping
		gem-mapper -T $number_of_threads -q 'offset-33' -I ${tmp_gem_index}.gem -i $reads -o $tmp_gem_map
		gem-2-sam -l -T $number_of_threads --expect-single-end-reads -q 'offset-33' -I ${tmp_gem_index}.gem -i ${tmp_gem_map}.map\
			| ${dn}/samtools view -Shu - \
			| ${dn}/samtools sort - $prefix
		rm ${tmp_gem_index}.gem ${tmp_gem_map}.map ${tmp_gem_index}.log
	
		;;

	peanut)
		tmp_index=${reference}.hdf5
		peanut index $reference $tmp_index
		peanut map --threads $number_of_threads $tmp_index $reads \
			| ${dn}/samtools view -Shu - \
            | ${dn}/samtools sort - $prefix
		rm $tmp_index
		;;

	tigermap)
		#mapping
		tigermap.py $reference $reads \
			| ${dn}/samtools view -Shu - \
			| ${dn}/samtools sort - $prefix
		;;

	*)
		error_message_exit "Unknown method '$method'."
		;;
esac

~/.smbl/bin/samtools index ${prefix}.bam

