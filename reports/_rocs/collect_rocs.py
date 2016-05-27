#! /usr/bin/env python3

import sys
import shutil
import os
import snakemake
import glob

"""
	experiment_dir -
	roc_dir - 
"""
def copy_report(
			experiment_dir,
			roc_dir,
			title="",
		):

	static_fn_o=os.path.join(experiment_dir,"3_evaluation.itref","roc","00000.roc")
	static_fn_n=os.path.join(roc_dir,"static.roc")

	fns=glob.glob(os.path.join(experiment_dir,"3_evaluation.itref","roc","*.roc"))
	fns=sorted(fns)
	
	try:
		itref_fn_o=fns[-1]
		itref_fn_n=os.path.join(roc_dir,"itref.roc")

		fns=glob.glob(os.path.join(experiment_dir,"3_evaluation.dyn","roc","*.roc"))
		fns=sorted(fns)
		dynamic_fn_o=fns[-1]
		dynamic_fn_n=os.path.join(roc_dir,"dynamic.roc")
	
		os.makedirs(roc_dir,exist_ok=True)

		#def symlink(original_path,new_path):
		#	new_dir=os.path.dirname(new_path)
		#	new_path_relative=os.path.relpath(original_path,new_dir)
		#	os.symlink(original_path,new_path_relative)

		def symlink(old,new):
			try:
				os.unlink(new)
			except:
				pass
			os.symlink("../"+old,new)


		symlink(static_fn_o,static_fn_n)
		symlink(dynamic_fn_o,dynamic_fn_n)
		symlink(itref_fn_o,itref_fn_n)
	except IndexError:
		print("Error, report {} could not be copied.".format(experiment_dir))

experiments=glob.glob('../../experiments/exp*/')
for experiment_dir in experiments:
	parts=experiment_dir.split("/")
	roc_dir=parts[-2]
	if roc_dir>="exp1" and roc_dir<="exp9":
		copy_report(experiment_dir,roc_dir)
