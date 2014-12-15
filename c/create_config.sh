#! /usr/bin/env bash

#set -x
set -euf -o pipefail

. _pipelinelib.sh



#cat /dev/null > $conf_file

echo "### SUBEXPERIMENT CONFIGURATION FILE
# keep BASH syntax
# 1=on, 0=off

# GENERAL
G_experiment_name=\"new_subexperiment\"
G_reference=\"your_reference.fa\"
G_reads=\"your_reads.fq\"
G_update_algorithm=\"parikh\"
G_number_of_threads=7
G_update_min_alignment_quality=1
G_update_majority=0.6
G_update_min_base_quality=0
G_update_min_coverage=3

# DYNAMIC WITH UNMAPPING
DU_on=1
DU_coverage_per_iteration=0.5

# DYNAMIC WITHOUT UNMAPPING
D_on=1
D_coverage_per_iteration=0.5

# STATIC
S_on=1
S_number_of_iterations=2

# READS DWGSIM PARAMETERS
R_alternative_reference=\"your_alternative_reference.fa\"
R_coverage=10
R_read_length=100
R_error_rate=0.020
R_rate_of_mutations=0.001
R_fraction_of_indels=0.10
R_prob_indel_extended=0.30
R_minimum_length_of_indel=1
R_prob_random_read=0.05
"

