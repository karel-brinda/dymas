.PHONY: all clean

all:
	gnuplot *.gp

	for f in "iterations_dm" "iterations_ir" "ir" "sm" "dm" ; do \
		svg2pdf $$f.svg $$f.pdf || \
		convert -density 200 $$f.svg $$f.pdf; \
	done

clean:
	rm -f *.svg *.pdf
