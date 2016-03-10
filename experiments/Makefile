SUBDIRS := $(wildcard exp*/.)

.PHONY : all $(SUBDIRS) data

all : $(SUBDIRS)

$(SUBDIRS) : data 
	    $(MAKE) -C $@

data :
	$(MAKE) -C exp.0.*
