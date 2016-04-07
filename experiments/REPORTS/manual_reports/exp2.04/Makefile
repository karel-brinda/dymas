.PHONY: all clean

all:
	gnuplot graphs1.gp
	gnuplot graphs2.gp

	for f in "iterations_dm" "iterations_ir" "ir" "sm" "dm" ; do \
		svg2pdf $$f.svg $$f.pdf || \
    convert -density 200 $$f.svg $$f.pdf; \
	done

clean:
	rm -f *.svg *.pdf
