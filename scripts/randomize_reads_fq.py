#! /usr/bin/env python3

import sys
import random

random.seed(0)

lines=["","","",""]
reads=[]

for i,line in enumerate(sys.stdin):
	lines[i%4]=line
	if i%4==3:
		reads.append("".join(lines))

random.shuffle(reads)
for x in reads:
	print(x,end="")