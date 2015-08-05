#! /usr/bin/env bash

#set -x
set -euf -o pipefail

old_method_calling=0


function help_message_exit {
	tput bold;
	tput setaf 7;
	echo 1>&2;
	echo "USAGE: $1" 1>&2;
	tput sgr0;
	echo 1>&2;
	echo "$2">&2;
	echo 1>&2;
	exit 1;
}

function important_message {
	echo;
	tput bold;
	tput setaf 6;
	echo "$1";
	tput sgr0;
	echo;
}

function error_message_exit {
	tput bold;
	tput setaf 1;
	echo "" 1>&2;
	echo "ERROR: $1" 1>&2;
	tput sgr0;
	echo 1>&2;
	exit 1;
}

function check_file {
	if [ ! -f $1 ] && [ ! -b $1 ] && [ ! -p $1 ];
	then
		error_message_exit "File '$1' does not exist.";
	fi
}

function check_dir {
	if [ ! -d $1 ];
	then
		error_message_exit "Directory '$1' does not exist.";
	fi
}

function check_select {
	echo;
}

function time_in_ms {
	echo $(( (`date +%s` * 1000) + 10#`date +%3N`))
}

function ms_diff {
	echo `bc <<< "scale=2; ( $2 - $1 )/1000"` s
}

function subexperiment_start {
	time_subexp_1=`time_in_ms`
	tput bold;
	tput setaf 3;
	echo;
	echo "===========================================================================";
	echo "EXPERIMENT '${1}' STARTED";
	echo "";
	echo "	(`date`)"
	echo "===========================================================================";
	tput sgr0;
}

function subexperiment_end {
	time_subexp_2=`time_in_ms`
	tput bold;
	tput setaf 3;
	echo;
	echo "===========================================================================";
	echo "EXPERIMENT '${1}' COMPLETED ";
	echo "";
	echo "	(`date`)"
	echo "";
	echo "   ...it lasted `ms_diff $time_subexp_1 $time_subexp_2`."
	echo "===========================================================================";
	echo;
	echo;
	tput sgr0;
}


function iteration_start {
	time_iter_1=`time_in_ms`
	tput bold;
	tput setaf 2; #green
	echo;
	echo "---------------------------------------------------------------------------";
	echo "Subexp. '${1}' -- iteration '${2}' (0..$3) started (`date "+%H:%M:%S"`)";
	echo "---------------------------------------------------------------------------";
	tput sgr0;
}

function iteration_end {
	time_iter_2=`time_in_ms`
	tput bold;
	tput setaf 2; #green
	echo "---------------------------------------------------------------------------";
	echo "Subexp. '${1}' -- iteration '${2}' (0..$3) completed (`date "+%H:%M:%S"`)";
	echo "   ...it lasted `ms_diff $time_iter_1 $time_iter_2`."
	echo "---------------------------------------------------------------------------";
	tput sgr0;
}

function procedure_start {
	time_proc_1=`time_in_ms`
	tput bold;
	tput setaf 4; #blue 
	echo "Procedure '$1' started (`date "+%H:%M:%S"`).";
	tput sgr0;
}

function procedure_end {
	time_proc_2=`time_in_ms`
	time_proc_diff=`ms_diff $time_proc_1 $time_proc_2`
	tput bold;
	tput setaf 4; #blue 
	echo "Procedure '$1' completed (`date "+%H:%M:%S"`). It lasted `ms_diff $time_proc_1 $time_proc_2`.";
	tput sgr0;
	echo "";
}

function ref_name_iteration {
	echo "fa/${1}.ref_${2}.fa"
}

#without .bam
function bam_name_iteration {
	echo "bam/${1}.aln_${2}"
}

function vcf_name_iteration {
	echo "vcf/${1}.dif_${2}.txt"
}

function subexperiment_prefix {
	echo "$1__$2"
}

