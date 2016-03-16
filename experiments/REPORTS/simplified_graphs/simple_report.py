#! /usr/bin/env python3

import sys
import shutil
import os
import snakemake
import glob
import argparse


def_x1="0.003"
def_x2="0.300"
def_y1="50"
def_y2="100"

def simple_report(
			experiment_dir,
			report_name,
			title="",
			x1=def_x1,
			x2=def_x2,
			y1=def_y1,
			y2=def_y2,
		):

	prefix=report_name

	command="""
		gnuplot -e "par_file='output/{file}';par_title='{title}';par_dir='{dir}';par_x1='{x1}';par_x2='{x2}';par_y1='{y1}';par_y2='{y2}';" plot_graph.gp 
		""".format(
			file=prefix,
			dir=experiment_dir,
			#title=report_name.replace("_","\\_"),
			#title=report_name,
			title="",
			#title=report_name.replace("_","\\_").replace("-","\\-"),
			#title=report_name.replace("_","").replace("-",""),
			x1=x1,
			x2=x2,
			y1=y1,
			y2=y2,
		)

	print(command.strip())
	snakemake.shell(command)
	try:
		snakemake.shell('svg2pdf output/{pref}.svg output/{pref}.pdf'.format(pref=prefix))
	except:
		pass

parser = argparse.ArgumentParser()
parser.add_argument(
		"experiment",
		type=str,
		help="display a square of a given number"
	)
parser.add_argument(
		"--x1",
		dest="x1",
		default=def_x1,
	)
parser.add_argument(
		"--x2",
		dest="x2",
		default=def_x2,
	)
parser.add_argument(
		"--y1",
		dest="y1",
		default=def_y1,
	)
parser.add_argument(
		"--y2",
		dest="y2",
		default=def_y2,
	)
args = parser.parse_args()

simple_report(
		experiment_dir=os.path.join("..","_rocs",args.experiment),
		report_name=args.experiment,
		x1=args.x1,
		x2=args.x2,
		y1=args.y1,
		y2=args.y2,
	)

