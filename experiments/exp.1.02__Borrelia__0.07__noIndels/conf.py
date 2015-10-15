import sys
sys.path.insert(0, "../")
from borrelia_conf import *

conf_mutrate=0.07
conf_updates_indels=False

conf_description+="mutrate {}; noindels;".format(conf_mutrate)