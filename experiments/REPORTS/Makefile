.PHONY: main_report simplified_graphs rocs clean dropbox

all: main_report simplified_graphs

main_report:
	$(MAKE) -C main_report

simplified_graphs: rocs
	$(MAKE) -C simplified_graphs

rocs:
	$(MAKE) -C _rocs

dropbox:
	cp -ar ../REPORTS ~/Dropbox/

clean:
	$(MAKE) -C main_report clean
	$(MAKE) -C manual_reports clean
	$(MAKE) -C simplified_graphs clean
	$(MAKE) -C _rocs clean
