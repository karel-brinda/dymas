SUBDIRS := $(wildcard exp*/.)

.PHONY : all $(SUBDIRS) data

all : $(SUBDIRS)
	$(MAKE) -C REPORTS

$(SUBDIRS) : data 
	    $(MAKE) -C $@

data :
	$(MAKE) -C exp0.*
