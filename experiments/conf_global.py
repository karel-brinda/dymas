import sys
sys.path.insert(0, "../../dymas")
import dymas

import rnftools
import smbl

conf_read_length=100
conf_allowed_delta=100
conf_contamination_coverage=0
conf_contamination_reference=None
conf_contamination_mutrate=0.03

conf_coverage_per_iteration=0.5

#conf_updates_indels=True

conf_title=""
conf_description=""

fq_fn="{}.fq".format(dymas.dir_reads)

def gp_style(i,nb):
	assert i<nb
	if nb!=1:
		red=int(255.0*i/(nb-1))
	else:
		red=0
	color = "".join(["#","%0.2X" % red,"00","%0.2X" % (255-red)])
	return 'set style line {i} lt 1 pt 1 lc rgb "{color}"'.format(i=i+1,color=color)
