import smbl

reference="../_experiments_data/human.chr21.fa"
reference_contamination="../_experiments_data/mouse.chr19.fa"
coverage=10
coverage_contamination=2

def gp_style(i,nb):
	assert i<nb
	if nb!=1:
		red=int(255.0*i/(nb-1))
	else:
		red=0
	color = "".join(["#","%0.2X" % red,"00","%0.2X" % (255-red)])
	return 'set style line {i} lt 1 pt {i} lc rgb "{color}"'.format(i=i+1,color=color)
