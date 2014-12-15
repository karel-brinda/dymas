#! /bin/bash

#set -o xtrace
set -o pipefail
set -e
. _pipelinelib.sh

## PARAMETERS CHECK ##

if [ $# -ne 2 ]; then
	help_message_exit \
		"${0##*/} experiment_configuration.conf mapper" \
		"Wrapper pro _subexperiment.sh."
fi

experiment_configuration=$1
mapper=$2

. _load_config.sh $experiment_configuration

log_prefix=log__${G_experiment_name}__$mapper
#report_name=report__${G_experiment_name}.html
tmp_log=${log_prefix}.tmp
html_log=${log_prefix}.html

_experiment.sh $experiment_configuration $mapper 2>&1 | tee $tmp_log

#echo "jdu to nalit do aha"
(aha --black --title "Subexperiment '$G_experiment_name'" < $tmp_log) > $html_log
rm $tmp_log

