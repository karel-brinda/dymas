SUBDIRS := $(wildcard exp*/.)

.PHONY : all $(SUBDIRS) data

all : $(SUBDIRS)
	$(MAKE) -C REPORT

$(SUBDIRS) : data 
	    $(MAKE) -C $@

data :
	$(MAKE) -C exp0.*
