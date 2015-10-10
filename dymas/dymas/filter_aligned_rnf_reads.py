#! /usr/bin/env python3

import sys
import argparse

def_i=13

parser = argparse.ArgumentParser(description='Take a subset of aligned reads (SAM to SAM conversion).')
parser.add_argument(
			'input_sam_fo',
			type=argparse.FileType('r'),
			metavar='input',
			help='Input SAM file (- for standard input).',
		)
parser.add_argument(
			'output_sam_fo',
			type=argparse.FileType('w+'),
			metavar='output',
			help='Output SAM file (- for standard output).',
		)
parser.add_argument(
			'-i',
			type=int,
			metavar='int',
			dest='i',
			default=def_i,
			help='Take every i-th read. [default: {}]'.format(def_i),
		)
args = parser.parse_args()

for x in args.input_sam_fo:
	#print(x)
	if x[0]=="@" or x.strip()=="":
		args.output_sam_fo.write(x)
		continue
	#print(x,file=sys.stderr)
	(left,_,_)=x.partition("\t")
	#print(left)
	parts=left.split("__")
	#print(parts,file=sys.stderr)
	if int(parts[1],16)%args.i==0:
		args.output_sam_fo.write(x)
