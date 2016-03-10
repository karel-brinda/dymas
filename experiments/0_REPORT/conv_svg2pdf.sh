#! /usr/bin/env bash

set -e

if [ $# -ne 1 ]; then
	echo "illegal number of parameters"
	exit 1
fi

SVG=$1
PDF=${SVG}.pdf

if [ ! -f $PDF ];
then
	echo SVG $SVG
	echo PDF $PDF
	echo
	svg2pdf $SVG $PDF
fi
