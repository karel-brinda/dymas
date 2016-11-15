import sys
sys.path.insert(0, "../")
from conf_exp3 import *

#################

consensus = dymas.Consensus_Py(
				call_snps=True,
				call_ins=True,
				call_dels=True,
			)

sorting = dymas.Sorting_SamTools()

pileup = dymas.Pileup_SamTools(baq=False)
