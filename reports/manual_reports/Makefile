#SUBDIRS := $(wildcard */.)

.PHONY: clean all

SHELL:=/bin/bash -o pipefail

all:
	@for a in $$(ls); do \
		if [ -d $$a ]; then \
			$(MAKE) -C $$a; \
		fi; \
	done;	

clean:
	@for a in $$(ls); do \
		if [ -d $$a ]; then \
			$(MAKE) -C $$a clean; \
		fi; \
	done;	
