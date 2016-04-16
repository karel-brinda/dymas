SUBDIRS := $(wildcard exp*/.)

.PHONY : all clean $(SUBDIRS) data

all : $(SUBDIRS)

$(SUBDIRS) : data 
	$(MAKE) -C $@

data :
	$(MAKE) -C exp0.*

clean:
	$(MAKE) -C $(SUBDIRS) clean
