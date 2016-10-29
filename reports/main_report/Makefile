MAIN = main
FIGURES := $(shell find aux -name "*.pdf" -type f)

SHELL:=/bin/bash -o pipefail

.PHONY: all clean

all : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex $(FIGURES)
	#find .. -type f -name "*.svg" -exec ./convert_svg2pdf.sh {} \;
	#latexmk -f -pdf --interaction=nonstopmode $(MAIN) || \ 

	pdflatex --interaction=nonstopmode $(MAIN)

$(MAIN).tex :
	#find ../.. -type f -name "*.svg" | xargs ../convert_svg2pdf.sh
	./main_texfile.py

clean :
	rm -fr aux/
	rm -f main.*