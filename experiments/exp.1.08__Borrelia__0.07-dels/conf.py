import sys
sys.path.insert(0, "../")
from borrelia_conf import *

conf_mutrate=0.07

conf_description+="mutrate {}; ".format(conf_mutrate)

#################

bwa = dymas.Mapping_BwaMem()

consensus = dymas.Consensus_Py(
				call_snps=True,
				call_ins=False,
				call_dels=True,
			)

sorting = dymas.Sorting_SamTools()

pileup = dymas.Pileup_SamTools(baq=False)
