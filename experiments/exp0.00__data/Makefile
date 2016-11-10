.PHONY: all clean

all: .yeast.complete

.yeast.complete:
	echo ">Saccharomyces_cerevisiae.R64-1-1" > yeast.fa
	curl -0 ftp://ftp.ensemblgenomes.org/pub/fungi/release-33/fasta/saccharomyces_cerevisiae/dna/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa.gz | \
		gunzip -c | \
		grep -v ">" | \
		perl -pi -e 's/\n//' | \
		fold -w80 \
	>> yeast.fa
	touch $@


clean:
	rm -fr *.fa .*complete