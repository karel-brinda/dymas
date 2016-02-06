#! /usr/bin/env python3

import os
import shutil
import snakemake

experiments_dir="../"


class Report:
	def __init__(self):
		self.auxdir="aux"
		self.tex="report.tex"
		os.makedirs(self.auxdir,exist_ok=True)
		self.experiments=[]

	def add_experiment(self,name):
		d=os.path.join(experiments_dir,name)
		nd=name
		ndf=os.path.join(self.auxdir,nd)

		self.experiments.append(
				[
					name,
					d,
					nd,
				]
			)


		os.makedirs(ndf,exist_ok=True)


		#
		# OVERVIEW
		#

		shutil.copy(
				os.path.join(d,"3_evaluation/0/pdf/_combined_4.pdf"),
				os.path.join(ndf,"dynamic.pdf"),
			)

		shutil.copy(
				os.path.join(d,"3_evaluation/1/pdf/_combined_4.pdf"),
				os.path.join(ndf,"iterative.pdf"),
			)


		#
		# DETAILS
		#

		# Static

		shutil.copy(
				os.path.join(d,"3_evaluation/1/pdf/00000.pdf"),
				os.path.join(ndf,"detail_stat.pdf"),
			)


		# Dynamic

		l=[x for x in os.listdir(os.path.join(d,"3_evaluation/0/pdf/")) if x[0]=="0"]
		l.sort()
		last=l[-1]

		shutil.copy(
				os.path.join(d,"3_evaluation/0/pdf/"+last),
				os.path.join(ndf,"detail_dyn.pdf"),
			)

		# Iterative referencing

		l=[x for x in os.listdir(os.path.join(d,"3_evaluation/1/pdf/")) if x[0]=="0"]
		l.sort()
		last=l[-1]

		shutil.copy(
				os.path.join(d,"3_evaluation/1/pdf/"+last),
				os.path.join(ndf,"detail_iter.pdf"),
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

				f.write(r"\section{Experiment: "+name.replace("_","\\_")+r"""}
					\begin{figure}[h]
						\newcommand{\DIR}{""" + os.path.join(self.auxdir,nd) + r"""}
						\newcommand{\graph}[1]{\includegraphics[width=6cm]{#1}}
						\begin{subfigure}[b]{1.0\textwidth}
							\includegraphics[width=8cm]{\DIR/dynamic.pdf}\includegraphics[width=8cm]{\DIR/iterative.pdf}
					        \caption{Comparison of all iterations.}
					    \end{subfigure}
					    \begin{subfigure}[b]{1.0\textwidth}
							\graph{\DIR/detail_stat.pdf}\graph{\DIR/detail_dyn.pdf}\graph{\DIR/detail_iter.pdf}
					        \caption{Categories of reads after ``classical mapping'', iterative referencing and dynamic mapping with unmapping.}
					    \end{subfigure}
						\caption{
					    	caption
					    }
					    \label{fig:main}
					\end{figure}
					\clearpage
					""")

			f.write(r"""
					\end{document}
				""")

			#snakemake.shell('pdflatex -interaction=nonstopmode report.tex')


r=Report()

for exp in [
		"exp.1.01__Borrelia__0.07-baq",
		"exp.1.02__Borrelia__0.07",
		"exp.1.03__Borrelia__0.07-ococo32",
		"exp.1.04__Borrelia__0.07-ococo16",
		"exp.1.05__Borrelia__0.07-delstats",
		"exp.1.06__Borrelia__0.07-indels",
		"exp.1.07__Borrelia__0.07-delstats-baq",
		"exp.1.08__Borrelia__0.07-dels",
	]:
	r.add_experiment(exp)

r.latex()