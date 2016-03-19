.PHONY: main_report simplified_graphs rocs

all: main_report simplified_graphs clean

main_report:
	$(MAKE) -C main_report

simplified_graphs: rocs
	$(MAKE) -C simplified_graphs

rocs:
	$(MAKE) -C _rocs

clean:
	git clean -fxd .
