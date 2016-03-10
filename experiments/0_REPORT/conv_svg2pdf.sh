#! /usr/bin/env bash

set -e

#if [ $# -ne 1 ]; then
#	echo "illegal number of parameters"
#	exit 1
#fi

for var in "$@"
do
	SVG=$var
	PDF=${SVG}.pdf

	if [ ! -f $PDF ] || [ $PDF -ot $SVG ] ;
	then
		echo SVG $SVG
		echo PDF $PDF
		echo
		svg2pdf $SVG $PDF
	fi
done
