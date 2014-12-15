#! /usr/bin/env bash

#set -x
set -euf -o pipefail

if [ $# -ne 1 ];
then
	help_message_exit \
		"${0##*/} config.conf" \
		"Compile and load configuration file. Used only by scripts."
fi

. _pipelinelib.sh

check_file $1

experiment_configuration=$1
compiled=${experiment_configuration}.compiled

function reads {
	. $1
	genome_size=`wc -c $G_reference|awk '{print $1}'`
	bc <<< "(($R_coverage * $genome_size)/$R_read_length)/1"
	#exit 1
}

function reads_per_iteration {
	. $1
	genome_size=`wc -c $G_reference|awk '{print $1}'`
	bc <<< "(($DU_coverage_per_iteration * $genome_size)/$R_read_length)/1"
	#exit 1
}

function iterations {
	bc <<< "((($1-1)/$2)/1)+1"
	#exit 1
}

if [ ! -f $compiled  ] || [ $experiment_configuration -nt $compiled ];
then
	echo "GOING TO COMPILE CONFIGURATION FILE $1"
	. $experiment_configuration

	cat $experiment_configuration > $compiled
	echo >> $compiled
	echo >> $compiled
	echo >> $compiled
	echo "#######################" >> $compiled
	echo "### COMPILED PART" >> $compiled
	
	#_G_number_of_reads=`count_fq.sh reads $G_reads`
	_G_number_of_reads=`reads $experiment_configuration`
	echo "_G_number_of_reads=$_G_number_of_reads" >> $compiled
	
	_DU_reads_per_iteration=`reads_per_iteration $experiment_configuration`
	echo "_DU_reads_per_iteration=$_DU_reads_per_iteration" >> $compiled

	#_DU_number_of_iterations=`subset_of_reads.py $G_reads $_DU_reads_per_iteration`
	_DU_number_of_iterations=`iterations $_G_number_of_reads $_DU_reads_per_iteration`
	echo $_DU_number_of_iterations
	echo "_DU_number_of_iterations=$_DU_number_of_iterations" >> $compiled
fi

. $compiled

