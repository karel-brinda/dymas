#! /usr/bin/env bash

#set -x
set -eu -o pipefail

. _pipelinelib.sh

if [ $# -ne 2 ];
then
	help_message_exit \
		"${0##*/} config.conf mapper" \
		"" 
fi

check_file $1
experiment_configuration=$1
. _load_config.sh $experiment_configuration
mapper=$2
prefix="${G_experiment_name}__$mapper"

report_name=report__${G_experiment_name}__$mapper.html


function process_roc_files {
	directory=$1
	echo "Running dwgsim_lave followed by roc2html." # "Error output of dwgsim_eval is redirected to /dev/null."
	for bamfile in ./$directory/*.bam
	do
		echo "processing '$bamfile'"
		dn=`dirname $bamfile`
		fn=`basename $bamfile`
		rocName="$dn/../reports/roc/${fn}.roc"
		dwgsim_lave -b $bamfile > $rocName
		roc2html.py $rocName "$dn/../reports/html/" "$dn/../reports/svg/"
	done
}

function subexp_statistics {
        mkdir -p $1/reports/svg/
        mkdir -p $1/reports/roc/
        mkdir -p $1/reports/html/

        process_roc_files $1/bam/
}

for D in $prefix/*; do
	echo
	echo
	echo $D
	echo
	if [ -d "${D}" ]; then
		subexp_statistics "${D}"   # your processing here
	fi
done

main_report.py ${experiment_configuration}.compiled $mapper > $report_name
