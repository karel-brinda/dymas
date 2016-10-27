SUBDIRS := $(wildcard exp*/.)

.PHONY : all clean $(SUBDIRS) data

V=1
SHELL:=/bin/bash -o pipefail

all : $(SUBDIRS)

$(SUBDIRS) : data 
	$(MAKE) -C $@
	tail -n +1 */*.tsv > results_edit_distance.tsv

data :
	$(MAKE) -C exp0.*

clean:
	@for a in $$(ls); do \
		if [ -e $$a/Makefile ]; then \
			$(MAKE) -C $$a clean; \
		fi; \
	done;	
