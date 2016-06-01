import sys
sys.path.insert(0, "../")
from conf_exp5 import *

conf_mutrate=0.07

conf_description+="mutrate {}; ".format(conf_mutrate)

##############################

bwa = dymas.Mapping_BwaMem()

consensus = dymas.Consensus_Ococo(
		strategy="majority",
		variant=16,
		remapping=True,
	)

sorting = dymas.Sorting_FakeNoSort()

pileup = dymas.Pileup_FakeEmpty()
