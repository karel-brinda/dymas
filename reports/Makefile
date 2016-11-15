.PHONY: all clean dropbox main_report simplified_graphs rocs

SHELL:=/bin/bash -o pipefail

all: main_report simplified_graphs manual_reports

main_report:
	$(MAKE) -C main_report

simplified_graphs: rocs
	$(MAKE) -C simplified_graphs

manual_reports: rocs
	$(MAKE) -C manual_reports

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
