SUBDIRS := $(wildcard exp*/.)

.PHONY : all clean $(SUBDIRS) data

all : $(SUBDIRS)

$(SUBDIRS) : data 
	$(MAKE) -C $@

data :
	$(MAKE) -C exp0.*

clean:
	@for a in $$(ls); do \
		if [ -d $$a ]; then \
			$(MAKE) -C $$a clean; \
		fi; \
	done;	
