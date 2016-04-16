.PHONY: all clean dropbox main_report simplified_graphs rocs

all: main_report simplified_graphs

main_report:
	$(MAKE) -C main_report

simplified_graphs: rocs
	$(MAKE) -C simplified_graphs

rocs:
	$(MAKE) -C _rocs

dropbox:
	cp -ar ../reports ~/Dropbox/

clean:
	@for a in $$(ls); do \
		if [ -d $$a ]; then \
			$(MAKE) -C $$a clean; \
		fi; \
	done;	
