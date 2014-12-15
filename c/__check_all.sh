#! /usr/bin/env bash

#set -x
set -euf -o pipefail

ok=1

function test_program {
	echo "Testing '$1'";
	command -v $1 >/dev/null 2>&1; 
	if [ $? -eq "0" ];
	then
		echo "     Ok.";
	else
		ok=0;
		echo "     Program '$1' is missing. Please install it from '$2'.";
		# if set $2, pritn install it from $2:
	fi
}

test_program bwa http://sourceforge.net/projects/bio-bwa/files/
test_program storm-nucleotide http://bioinfo.lifl.fr/yass/iedera_solid/storm/
test_program gem-indexer http://sourceforge.net/projects/gemlibrary/files/
test_program gem-mapper http://sourceforge.net/projects/gemlibrary/files/
test_program gem-2-sam http://sourceforge.net/projects/gemlibrary/files/

test_program python http://python.org
test_program samtools http://sourceforge.net/projects/samtools/files/samtools/
test_program dwgsim http://davetang.org/wiki/tiki-index.php?page=DWGSIM
test_program dwgsim_eval http://davetang.org/wiki/tiki-index.php?page=DWGSIM
test_program bgzip http://sourceforge.net/projects/samtools/files/samtools/
test_program tabix http://sourceforge.net/projects/samtools/files/samtools/
test_program vcf-consensus http://vcftools.sourceforge.net/

test_program ffmpeg //www.ffmpeg.org/download.html
test_program aha https://github.com/theZiz/aha

echo
if [ "$ok" -eq "1" ]; then
	echo "All required programs are installed."
else
	echo "Some required programs are missing."
fi
