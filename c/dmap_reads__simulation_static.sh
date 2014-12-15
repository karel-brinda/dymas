#! /bin/bash

#set -x
set -euf -o pipefail

. _pipelinelib.sh

## PARAMETERS CHECK ##

if [ $# -ne 2 ]; then
	help_message_exit \
		"${0##*/} experiment_configuration.conf mapper" \
		""
fi

experiment_configuration=$1
mapper=$2

check_file $experiment_configuration
. _load_config.sh $experiment_configuration
export G_number_of_threads

prefix=`subexperiment_prefix ${G_experiment_name} $mapper`
directory=$prefix/static

check_file $G_reference
check_file $G_reads
directory=`realpath $directory`
mkdir -p $directory

rm -fR $directory/bam/*
rm -fR $directory/fa/*
rm -fR  $directory/reports/*
rm -fR $directory/vcf/*

mkdir -p $directory/bam/
mkdir -p $directory/fa/
mkdir -p $directory/reports/
mkdir -p $directory/vcf/

####################
## STATIC MAPPING ##
####################

cp $G_reference $directory/`ref_name_iteration $prefix 0000`
max_nb_of_iteration=$(( S_number_of_iterations - 1 ))

for iteration in `seq 0 $max_nb_of_iteration`;
do
	let "next_iteration=iteration+1"

	# leading zeros
	iteration=`printf %04d $iteration`
	next_iteration=`printf %04d $next_iteration`

	iteration_start $prefix $iteration $max_nb_of_iteration

	procedure_start "mapping reads"
	map_reads.sh \
		$mapper\
		$directory/`ref_name_iteration $prefix $iteration` \
		$G_reads \
		$directory/`bam_name_iteration $prefix $iteration` \
	> /dev/null
	procedure_end "mapping reads"
	
	procedure_start "updating reference"
	if [ $old_method_calling != "1" ]; then
		samtools mpileup\
			--min-MQ $G_update_min_alignment_quality \
			$directory/`bam_name_iteration $prefix $iteration`.bam | \
		call_variants\
			--calling-alg $G_update_algorithm \
			--reference $directory/`ref_name_iteration $prefix $iteration` \
			--min-coverage $G_update_min_coverage \
			--min-base-qual $G_update_min_base_quality \
			--accept-level $G_update_majority \
		> $directory/`ref_name_iteration $prefix $next_iteration` || echo "tady se to taky nepovedlo"
	else
		update_reference.py\
			$directory/`ref_name_iteration $prefix $iteration` \
			$directory/`bam_name_iteration $prefix $iteration`.bam \
			$directory/`ref_name_iteration $prefix $next_iteration` \
		> $directory/`vcf_name_iteration $prefix $iteration`
	fi
	procedure_end "updating reference"

	iteration_end $prefix $iteration $max_nb_of_iteration
done

