.PHONY: all clean experiments reports

SHELL:=/bin/bash -o pipefail

all: experiments reports

clean:
	$(MAKE) -C reports clean
	$(MAKE) -C experiments clean

experiments:
	$(MAKE) -C experiments

reports: experiments
	$(MAKE) -C reports
