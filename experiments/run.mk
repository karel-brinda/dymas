.PHONY: clean run rm1 rm2 rm3 rm5 view

V=1
SHELL:=/bin/bash -o pipefail

run: 1_reads.fq .dyn.complete .itref.complete evaluation.html .edit_dist.compl .updates.compl

clean: rm1 rm2 rm3 rm5
	rm -fr .*.compl
	rm -fr .*.complete

rm1:
	rm -fr 1_reads*

rm2:
	rm -fr 2_alignments.*

rm3:
	rm -fr 3_evaluation*

rm5:
	rm -fr *.tsv

1_reads.fq:
	snakemake -s Snakefile.1_reads --cores -p

.dyn.complete: 1_reads.fq
	snakemake -s Snakefile.2_1_exp_dyn --cores -p

.itref.complete: 1_reads.fq
	snakemake -s Snakefile.2_2_exp_itref --cores -p

evaluation.html: .dyn.complete .itref.complete
	snakemake -s Snakefile.3_eval --cores -p

.edit_dist.compl: .dyn.complete .itref.complete
	../../scripts/run_edit_distances.sh .
	touch $@

.updates.compl: .dyn.complete .itref.complete
	../../scripts/run_updates.sh .
	touch $@

view:
	open 3_evaluation.html || google-chrome 3_evaluation.html

