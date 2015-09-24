#! /usr/bin/env bash

#set -e

for d in `ls -d exp.??__*/`; do
	echo
	echo
	echo "================="
	echo "$d"
	echo "================="
	echo
	(cd $d && ./run.sh)	
done

