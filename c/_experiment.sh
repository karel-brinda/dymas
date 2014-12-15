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

prefix=`subexperiment_prefix ${G_experiment_name} $mapper`
mkdir -p $prefix

##########################################################
subexperiment_start $prefix

#rm -f ${prefix}.*

## DYNAMIC MAPPING WITH UNMAPPING ##

if [ $DU_on -eq "1" ]; then
	important_message "ON:  Dynamic mapping with unmapping"
	dmap_reads__simulation_dynamic_with_unmapping.sh $experiment_configuration $mapper
else
	important_message "OFF: Dynamic mapping with unmapping"		
fi

## DYNAMIC MAPPING WITHOUT UNMAPPING ##

if [ $D_on -eq "1" ]; then
	important_message "ON:  Dynamic mapping without unmapping"
	important_message "	... but it is not implemented, yet."
else
	important_message "OFF: Dynamic mapping without unmapping"

fi

## STATIC MAPPING ##
if [ $S_on -eq "1" ]; then
	important_message "ON:  Static mapping"
	mkdir -p $prefix/static
	dmap_reads__simulation_static.sh $experiment_configuration $mapper
else
	important_message "OFF: Static mapping"
fi


## EVALUATION ##

procedure_start "making statistics for bam files"
#make_experiment_statistics.sh $experiment_configuration $mapper
procedure_end "making statistics for bam files"

subexperiment_end $prefix

##########################################################

