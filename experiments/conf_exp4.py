from conf_global import *

conf_reference="../exp0.00__data/yeast.fa"
conf_coverage=10

conf_mutrate=0.03
conf_description+="mutrate {}; ".format(conf_mutrate)

conf_title+="Yeast (saccharomyces_cerevisiae)"
#conf_description+="cov 5; "

haploid_mode=False

bwa = dymas.Mapping_Bowtie2()
