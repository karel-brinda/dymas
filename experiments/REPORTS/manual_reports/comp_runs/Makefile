.PHONY: all clean

all:
	~/.smbl/bin/gnuplot5 *.gp
	../../conv_svg2pdf.sh manual_exp1.svg
	../../conv_svg2pdf.sh manual_exp2.svg

clean:
	rm -fr *.svg
	rm -fr *.pdf
