.PHONY: all clean

SCRIPT=./simple_report.py

#EXPERIMENTS := $(shell find ../_rocs/ -type d -name "exp.*")
EXPERIMENTS := $(shell ls "../_rocs" | grep "^exp.")
ROCS := $(shell find ../_rocs/ -type f -name "*.roc")


all: $(ROCS)

	for exp in $(EXPERIMENTS) ; do \
		echo $$exp ; \
		$(SCRIPT) $$exp ; \
	done

clean:
	rm -fr output/*.svg
	rm -fr output/*.pdf