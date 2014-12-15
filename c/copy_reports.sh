#! /usr/bin/env bash

#set -x
set -euf -o pipefail

dr="/home/karel/Dropbox/tmp_reporty/"

echo "$1"
to_copy=`find -name '*.html';find -name '*.roc';find -name '*.svg'`
#echo $to_copy
for td in $to_copy
do
	dn=`dirname $td`
	mkdir -p "$dr/$dn"
	cp -v $td $dr/$td
done

