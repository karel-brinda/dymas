import sys
sys.path.insert(0, "../")
from conf_exp3 import *

##############################

consensus = dymas.Consensus_Ococo(
		strategy="majority",
		variant=16,
		remapping=True,
	)

sorting = dymas.Sorting_FakeNoSort()

pileup = dymas.Pileup_FakeEmpty()