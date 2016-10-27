#! /usr/bin/env python3

import sys
import re

alns=0

freqs={
	"M":0,
	"X":0,
	"I":0,
	"D":0,
	"S":0,
	"H":0,
	"=":0,
}


r=re.compile(r'[0-9]*.')
r_md=re.compile(r'MD:Z:([0-9A-Z\^]*)')	

for line in sys.stdin:
	if line[0]=="@":
		continue
	parts=line.split()
	cigar=parts[5]

	if cigar=="*":
		continue

	alns+=1

	freqs_aln={
		"M":0,
		"X":0,
		"I":0,
		"D":0,
		"S":0,
		"H":0,
		"=":0,
	}


	ops=r.findall(cigar)

	dels=0

	for x in ops:
		op=x[-1]
		count=int(x[:-1])
		freqs_aln[op]+=count

	#correction - = vs. X
	ops2=r_md.findall(line)
	md=r_md.findall(line)
	md=md[0]
	dels_mismatches=md.count("A")+md.count("C")+md.count("G")+md.count("T")
	mismatches=dels_mismatches-freqs_aln['D']
	#print(md, dels_mismatches, mismatches)

	if freqs_aln['M']>0:
		assert freqs_aln['X']==0
		assert freqs_aln['=']==0
		freqs_aln['X']=mismatches
		freqs_aln['=']=freqs_aln['M']-mismatches
		freqs_aln['M']=0

	for k in freqs:
		freqs[k]+=freqs_aln[k]


ks=sorted(freqs.keys())
print("#op\tper r\ttotal")
for k in ks:
	print("{}\t{:3.2f}\t{}".format(k,freqs[k]/alns,freqs[k]))