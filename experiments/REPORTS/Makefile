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
	git clean -fxd .
