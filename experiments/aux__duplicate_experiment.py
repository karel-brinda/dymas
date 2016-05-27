#! /usr/bin/env python3

import sys
import snakemake
import os
import argparse
import glob
import shutil

def cp_run(orig_exp, new_exp, orig_run_dir, new_run_dir):
	os.makedirs(new_run_dir,exist_ok=True)
	for x in ["Snakefile.1_reads","Snakefile.2_1_exp_dyn","Snakefile.2_2_exp_itref","Snakefile.3_eval","conf.py","Makefile"]:
		o=os.path.join(orig_run_dir,x)
		n=os.path.join(new_run_dir,x)
		if os.path.islink(o):
			linkto = os.readlink(o)
			os.symlink(linkto, n)
		else:
			shutil.copy2(o,n)

	nconf_fn=os.path.join(new_run_dir,"conf.py")
	with open(nconf_fn) as f:
		conf=f.read()
	conf=conf.replace(
			"from conf_{} import *".format(orig_exp),
			"from conf_{} import *".format(new_exp),
		)
	with open(nconf_fn,"w+") as f:
		f.write(conf)

def cp_experiment(orig_exp,new_exp):

	runs=glob.glob("{}*/".format(orig_exp))
	runs=sorted(runs)

	for orig_run in runs:
		new_run=orig_run.replace(orig_exp, new_exp)
		
		cp_run(orig_exp, new_exp, orig_run, new_run)



parser = argparse.ArgumentParser()
parser.add_argument(
		"orig",
		type=str,
		help="Original experiment, example: 'exp1'"
	)
parser.add_argument(
		"new",
		type=str,
		help="New experiment, example: 'exp2'"
	)
args = parser.parse_args()

cp_experiment(args.orig,args.new)