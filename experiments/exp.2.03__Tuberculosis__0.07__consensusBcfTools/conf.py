import sys
sys.path.insert(0, "../")
from tuberculosis_conf import *

conf_mutrate=0.07

conf_description+="mutrate {}; BcfTools consensus;".format(conf_mutrate)
