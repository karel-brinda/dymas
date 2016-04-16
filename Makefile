.PHONY: all clean experiments reports

all: experiments reports

clean:
	$(MAKE) -C reports clean
	$(MAKE) -C experiments clean

experiments:
	$(MAKE) -C experiments

reports: experiments
	$(MAKE) -C reports
