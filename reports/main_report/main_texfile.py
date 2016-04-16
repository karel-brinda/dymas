#! /usr/bin/env python3

import glob

import os
import shutil
import snakemake

experiments_dir="../../experiments/"

exp_pattern = "exp*/"
lex_min_exp = "exp1"
lex_max_exp = "exp9"

def copy(src,dest):
	print("Copying '{}' to '{}'".format(src, dest))
	shutil.copy(src,dest)

class Report:
	def __init__(self):
		self.auxdir="aux"
		self.tex="main.tex"
		os.makedirs(self.auxdir,exist_ok=True)
		self.experiments=[]

	def add_experiment(self,name):
		d=os.path.join(experiments_dir,name)
		nd=name
		ndf=os.path.join(self.auxdir,nd)


		os.makedirs(ndf,exist_ok=True)


		#
		# OVERVIEW
		#

		copy(
				os.path.join(d,"3_evaluation.dyn/graphics/_combined_2.pdf"),
				os.path.join(ndf,"dynamic.pdf"),
			)

		copy(
				os.path.join(d,"3_evaluation.itref/graphics/_combined_2.pdf"),
				os.path.join(ndf,"iterative.pdf"),
			)


		#
		# DETAILS
		#

		# Static

		copy(
				os.path.join(d,"3_evaluation.itref/graphics/00000.pdf"),
				os.path.join(ndf,"detail_stat.pdf"),
			)


		# Dynamic

		l=[x for x in os.listdir(os.path.join(d,"3_evaluation.dyn/graphics/")) if x[0]=="0" and x[-4:]==".pdf"]
		l.sort()
		last=l[-1]

		copy(
				os.path.join(d,"3_evaluation.dyn/graphics/"+last),
				os.path.join(ndf,"detail_dyn.pdf"),
			)

		# Iterative referencing

		l=[x for x in os.listdir(os.path.join(d,"3_evaluation.itref/graphics/")) if x[0]=="0" and x[-4:]==".pdf"]
		l.sort()
		last=l[-1]

		copy(
				os.path.join(d,"3_evaluation.itref/graphics/"+last),
				os.path.join(ndf,"detail_iter.pdf"),
			)

		self.experiments.append(
				[
					name,
					d,
					nd,
				]
			)




	def latex(self):
		with open(self.tex,"w+") as f:
			f.write(r"""
					\documentclass[12pt,a4paper]{article}
					\usepackage[T1]{fontenc}
					\usepackage[utf8]{inputenc}
					\usepackage{lmodern}
					\usepackage[english]{babel}
					\usepackage{amsmath}
					\usepackage{amsfonts}
					\usepackage{fullpage}
					\usepackage{graphicx}
					\usepackage{caption}
					\usepackage{subcaption}
					\begin{document}
				""")


			for (name,d,nd) in self.experiments:

				f.write(r"\section{"+name.replace("_","\\_")+r"""}
					\begin{figure}[h]
						\newcommand{\DIR}{""" + os.path.join(self.auxdir,nd) + r"""}
						\newcommand{\graph}[1]{\includegraphics[width=6cm]{#1}}
						\begin{subfigure}[b]{1.0\textwidth}
							\includegraphics[width=8cm]{\DIR/dynamic.pdf}\includegraphics[width=8cm]{\DIR/iterative.pdf}
					        \caption{Comparison of all iterations.}
					    \end{subfigure}
					    \begin{subfigure}[b]{1.0\textwidth}
							\graph{\DIR/detail_stat.pdf}\graph{\DIR/detail_dyn.pdf}\graph{\DIR/detail_iter.pdf}
					        \caption{Improvement of alignment using dynamic mapping and iterative referencing.}
					    \end{subfigure}
						%\caption{
					    %	caption
					    %}
					    \label{fig:main}
					\end{figure}
					\clearpage
					""")

			f.write(r"""
					\end{document}
				""")

			#snakemake.shell('pdflatex -interaction=nonstopmode report.tex')


r=Report()

exps = sorted(glob.glob(os.path.join(experiments_dir,exp_pattern)))
exps = [x.replace(experiments_dir,"") for x in exps]
print(exps)
exps = [x for x in exps if x >= lex_min_exp and x<lex_max_exp]

print(exps)

for exp in exps:
	try:
		r.add_experiment(exp)
	except Exception as e:
		print("Error: Experiment {} could not be added".format(exp))
		print(str(e))

r.latex()
