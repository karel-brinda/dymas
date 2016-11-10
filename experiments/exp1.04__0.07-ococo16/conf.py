import sys
sys.path.insert(0, "../")
from conf_exp1 import *

##############################

bwa = dymas.Mapping_BwaMem()

consensus = dymas.Consensus_Ococo(
		strategy="majority",
		variant=16,
		remapping=True,
	)

sorting = dymas.Sorting_FakeNoSort()

pileup = dymas.Pileup_FakeEmpty()
