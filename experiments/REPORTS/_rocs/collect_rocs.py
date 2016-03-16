#! /usr/bin/env python3

import sys
import shutil
import os
import snakemake
import glob

def copy_report(
			experiment_dir,
			roc_dir,
			title="",
		):
	os.makedirs(roc_dir,exist_ok=True)

	static_fn_o=os.path.join(experiment_dir,"3_evaluation","1","roc","00000.roc")
	static_fn_n=os.path.join(roc_dir,"static.roc")

	fns=glob.glob(os.path.join(experiment_dir,"3_evaluation","1","roc","*.roc"))
	fns=sorted(fns)
	itref_fn_o=fns[-1]
	itref_fn_n=os.path.join(roc_dir,"itref.roc")

	fns=glob.glob(os.path.join(experiment_dir,"3_evaluation","0","roc","*.roc"))
	fns=sorted(fns)
	dynamic_fn_o=fns[-1]
	dynamic_fn_n=os.path.join(roc_dir,"dynamic.roc")

	shutil.copyfile(static_fn_o,static_fn_n)
	shutil.copyfile(dynamic_fn_o,dynamic_fn_n)
	shutil.copyfile(itref_fn_o,itref_fn_n)
	shutil.copystat(static_fn_o,static_fn_n)
	shutil.copystat(dynamic_fn_o,dynamic_fn_n)
	shutil.copystat(itref_fn_o,itref_fn_n)

experiments=glob.glob('../../exp.*/')
for experiment_dir in experiments:
	parts=experiment_dir.split("/")
	roc_dir=parts[-2]
	if roc_dir>"exp.1" and roc_dir<"exp.3":
		copy_report(experiment_dir,roc_dir)