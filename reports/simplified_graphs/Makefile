.PHONY: all clean

ROCS := $(shell find ../_rocs/ -type f -name "*.roc")

all: $(ROCS)

	ls "../_rocs" | grep "^exp." | parallel -P 10 ./simple_report.py {}

clean:
	rm -fr output/*.svg
	rm -fr output/*.pdf
