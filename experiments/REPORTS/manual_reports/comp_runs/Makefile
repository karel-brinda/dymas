.PHONY: all clean

all:
	~/.smbl/bin/gnuplot5 *.gp
	../../conv_svg2pdf.sh exp1.svg
	../../conv_svg2pdf.sh exp2.svg

clean:
	rm -fr *.svg
	rm -fr *.pdf
