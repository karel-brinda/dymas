.PHONY: all clean

all:
	gnuplot *.gp
	find . -name '*.svg' | parallel -P 10 svg42pdf -m 'inkscape' {} {.}.pdf

clean:
	rm -f *.svg *.pdf
