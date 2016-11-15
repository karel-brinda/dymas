.PHONY: all clean

SHELL:=/bin/bash -o pipefail

all:
	gnuplot *.gp
	find . -name '*.gp' | parallel --no-notice gnuplot {}
	find . -name '*.svg' | parallel --no-notice -P 10 svg42pdf -m 'inkscape' {} {.}.pdf

clean:
	rm -f *.svg *.pdf
