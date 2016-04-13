#! /usr/bin/env bash

set -x

if [ $# -ne 1 ]; 
	then echo "illegal number of parameters"
	exit 1
fi

target_dir=$(realpath $1)

for d in `ls -d exp.?.??__*/`; do
	(
		echo 
		echo "directory $d"
		cd $d
		mkdir -p $target_dir/$d
		cp -fr 3_evaluation* $target_dir/$d
	)
done

