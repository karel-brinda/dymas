import sys
sys.path.insert(0, "../")
from conf_exp3 import *

conf_mutrate=0.07

conf_description+="mutrate {}; ".format(conf_mutrate)

#################

bwa = dymas.Mapping_Bowtie2(local_alignment=True)

consensus = dymas.Consensus_Py(
				call_snps=True,
				call_ins=False,
				call_dels=False,
			)

sorting = dymas.Sorting_SamTools()

pileup = dymas.Pileup_SamTools(baq=False)
