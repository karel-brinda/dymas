.PHONY: all clean

all: .yeast.complete .chr21.complete

.yeast.complete:
	echo ">Saccharomyces_cerevisiae.R64-1-1" > yeast.fa
	curl -0 ftp://ftp.ensemblgenomes.org/pub/fungi/release-33/fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa.gz | \
		gunzip -c | \
		grep -v ">" | \
		perl -pi -e 's/\n//' | \
		fold -w80 \
	>> yeast.fa
	touch $@

.chr21.complete:
	echo ">chr21" > chr21.fa
	curl -0 http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr21.fa.gz | \
		gunzip -c | \
		grep -v ">" | \
		perl -pi -e 's/\n//' | \
		perl -nle 'print uc' | \
		sed '/^>/! s/[^AGCT]/N/g' | \
		perl -pi -e 's/N//g' | \
		fold -w80 \
	>> chr21.fa
	touch $@

clean:
	rm -fr *.fa .*complete *.fai
