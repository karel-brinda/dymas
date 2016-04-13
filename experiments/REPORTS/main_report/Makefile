MAIN = main
FIGURES := $(shell find aux -name "*.pdf" -type f)

.PHONY: all clean view 
.SILENT: all

all : $(MAIN).pdf

$(MAIN).pdf : $(MAIN).tex $(FIGURES)
	#find .. -type f -name "*.svg" -exec ./convert_svg2pdf.sh {} \;
	#latexmk -f -pdf --interaction=nonstopmode $(MAIN) || \ 

	pdflatex --interaction=nonstopmode $(MAIN)

$(MAIN).tex :
	#find ../.. -type f -name "*.svg" | xargs ../convert_svg2pdf.sh
	./main_texfile.py

view:
	(open $(MAIN).pdf \
	|| acroread $(MAIN).pdf \
	|| evince $(MAIN).pdf) 2> /dev/null > /dev/null &

clean :
	rm -fr aux/
	rm -f main.pdf
	rm -f main.aux
	rm -f main.log
	#cd ..
	#find . -type f -name "*.svg.pdf" | xargs rm

