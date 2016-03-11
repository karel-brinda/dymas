MAIN = main
FIGURES := $(shell find figures -name "*.pdf" -type f)
SOURCES := $(MAIN).tex $(shell find . -name "*.tex" -type f)

.PHONY: all clean
.SILENT: all

all : $(MAIN).pdf

$(MAIN).pdf : $(SOURCES) $(FIGURES)
	#find .. -type f -name "*.svg" -exec ./conv_svg2pdf.sh {} \;
	find .. -type f -name "*.svg" | xargs ./conv_svg2pdf.sh
	./make_pdf.py
	latexmk -f -pdf --interaction=nonstopmode $(MAIN)

edit: $(MAIN).pdf
	(open $(MAIN).tex \
	|| texstudio $(MAIN).tex \
	|| texedit $(MAIN).tex) 2> /dev/null > /dev/null &

view:
	(open $(MAIN).pdf \
	|| acroread $(MAIN).pdf \
	|| evince $(MAIN).pdf) 2> /dev/null > /dev/null &

clean :
	rm -fr aux/
	latexmk -CA
	cd ..
	find . -type f -name "*.svg.pdf" | xargs rm

