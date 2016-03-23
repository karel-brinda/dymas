#! /usr/bin/env bash

set -e
set -o xtrace

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
		#cat $SVG | perl -e "s/fill\ =\ 'white'/fill\ =\ 'none'/g;" | svg2pdf > $PDF
		(cat $SVG | sed -e "s/'white'/'none'/" | svg2pdf > $PDF) || \
		convert $SVG $PDF
			#convert -density 300 $SVG $PDF
	fi
done
