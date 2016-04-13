.PHONY: all clean

all:
	export PATH=$PATH:~/.smbl/bin
	gnuplot5 *.gp
	../../convert_svg2pdf.sh *.svg

	for f in *.svg ; do \
		svg2pdf $$f $$f.pdf || \
		convert -density 200 $$f $$f.pdf; \
	done

	rename 's/\.svg\.pdf$//\.pdf/' *.svg.pdf
	#../../convert_svg2pdf.sh manual_exp1.svg
	#../../convert_svg2pdf.sh manual_exp2.svg
	#../../convert_svg2pdf.sh manual_exp4.svg
	#../../convert_svg2pdf.sh manual_exp5.svg

clean:
	rm -fr *.svg
	rm -fr *.pdf
