from conf_global import *

conf_reference="../exp0.00__data/chr21.fa"
conf_coverage=10

conf_mutrate=0.03
conf_description+="mutrate {}; ".format(conf_mutrate)

conf_title+="Human chr21"
#conf_description+="cov 5; "

haploid_mode=True

bwa = dymas.Mapping_BwaMem()
