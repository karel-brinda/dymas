import os
import smbl
import functools
import shutil
import gzip
import inspect
import termcolor

# todo: tabix

from .Chain_Chainer import Chain_Chainer
from .Chain import Chain

from .Pileup_FakeEmpty import *

class Experiment:

	def __init__(self,
				experiment_name,
				starting_reference_fasta_fn,
				mapping_object,
				reads_object,
				pileup_object,
				consensus_object,
				sorting_object,
				remapping=True,
			):

		self.experiment_name=experiment_name

		self.starting_reference_fasta_fn=starting_reference_fasta_fn
		self.mapping_object=mapping_object
		self.reads_object=reads_object
		self.pileup_object=pileup_object
		self.consensus_object=consensus_object
		self.sorting_object=sorting_object
		self.remapping=remapping

		self.register_smbl_rules()

	def info_msg(self,iteration):
		function=inspect.stack()[1][3]

		txt_line="[{directory}] [{function}] [iteration {it}/{all_it}]".format(
			directory=os.getcwd(),
			function=function,
			it=iteration,
			all_it=self.iterations,
		)
		sep_line=len(txt_line)*"="
		sep_line=termcolor.colored(sep_line,'red')
		txt_line=termcolor.colored(txt_line,'red')
		print(sep_line)
		print(txt_line)
		print(sep_line)

	def input(self):
		return [
				self.fasta_fn(self.iterations),
				#self.full_inverted_chain_fn(self.iterations-1),
				[self.rnf_lifted_bam_fn(it) for it in range(self.iterations)]
			]

	@property
	def iterations(self):
	    return self.reads_object.iterations

	@staticmethod
	def _iteration(iteration,suffix=""):
		return "{}{{}}".format(iteration).zfill(5+2).format(suffix)

	###########

	def fasta_fn(self,iteration):
		return os.path.join(self.experiment_name,"1_reference",self._iteration(iteration,".fa"))

	def fastq_fn(self,iteration):
		return os.path.join(self.experiment_name,"2_reads",self._iteration(iteration,".fq"))

	def unsorted_bam_fn(self,iteration):
		return os.path.join(self.experiment_name,"3.1_unsorted_bam",self._iteration(iteration,".bam"))

	def sorted_bam_fn(self,iteration):
		return os.path.join(self.experiment_name,"3.2_sorted_bam",self._iteration(iteration,".bam"))

	def rnf_lifted_bam_fn(self,iteration):
		return os.path.join(self.experiment_name,"3.3_rnf_lifted_bam",self._iteration(iteration,".bam"))

	def pileup_fn(self,iteration):
		return os.path.join(self.experiment_name,"4_pileup",self._iteration(iteration,".pileup.gz"))

	def compressed_vcf_fn(self,iteration):
		return os.path.join(self.experiment_name,"5_vcf",self._iteration(iteration,".vcf.gz"))

	def basic_chain_fn(self,iteration):
		return os.path.join(self.experiment_name,"6.1_basic_chain",self._iteration(iteration,".chain"))

	def full_chain_fn(self,iteration):
		return os.path.join(self.experiment_name,"6.2_full_chain",self._iteration(iteration,".chain"))

	def full_inverted_chain_fn(self,iteration):
		return os.path.join(self.experiment_name,"6.3_full_inverted_chain",self._iteration(iteration,".chain"))

	def tmp_dir(self):
		return os.path.join(self.experiment_name,"tmp")

	###########

	def register_smbl_rules(self):
		smbl.utils.Rule(
				input=self.starting_reference_fasta_fn,
				output=self.fasta_fn(0),
				run=lambda: shutil.copyfile(
						self.starting_reference_fasta_fn,
						self.fasta_fn(0)
					),
			)

		for iteration in range(self.iterations):

			# create_reads
			smbl.utils.Rule(
				input=[
						self.reads_object.required,
					],
				output=self.fastq_fn(iteration),
				run=functools.partial(self.create_reads,iteration=iteration),
			)

			# map_reads
			smbl.utils.Rule(
				input=[
						self.fasta_fn(iteration),
						self.fasta_fn(iteration)+".fai",
						self.fastq_fn(iteration),
						self.mapping_object.required,
					],
				output=self.unsorted_bam_fn(iteration),
				run=functools.partial(self.map_reads,iteration=iteration),
			)

			# sort_bam
			smbl.utils.Rule(
				input=[
						self.unsorted_bam_fn(iteration),
						smbl.prog.SAMTOOLS,
					],
				output=self.sorted_bam_fn(iteration),
				run=functools.partial(self.sort_bam,iteration=iteration),
			)

			# create_pileup
			smbl.utils.Rule(
				input=[
						self.pileup_object.required,
						self.fasta_fn(iteration),
						self.unsorted_bam_fn(iteration),
						self.sorted_bam_fn(iteration) if not isinstance(self.pileup_object,Pileup_FakeEmpty) else [],
					],
				output=self.pileup_fn(iteration),
				run=functools.partial(self.create_pileup,iteration=iteration),
			)

			# create_consensus
			smbl.utils.Rule(
				input=[
						self.consensus_object.required,
						self.fasta_fn(iteration),
						self.pileup_fn(iteration),
					],
				output=[
						self.compressed_vcf_fn(iteration),
					],
				run=functools.partial(self.create_consensus,iteration=iteration),
			)

			# update_reference
			smbl.utils.Rule(
				input=[
						self.consensus_object.required,
						self.fasta_fn(iteration),
						self.fasta_fn(iteration)+".fai",
						self.compressed_vcf_fn(iteration),
					],
				output=[
						self.fasta_fn(iteration+1),
						self.basic_chain_fn(iteration),
					],
				run=functools.partial(self.update_reference,iteration=iteration),
			)

			# create_full_chain
			smbl.utils.Rule(
				input=[
						self.full_chain_fn(iteration-1),
						self.basic_chain_fn(iteration),
					] if iteration>0 else self.basic_chain_fn(iteration),
				output=[
						self.full_chain_fn(iteration),
					],
				run=functools.partial(self.create_full_chain,iteration=iteration),
			)

			# create_full_inverted_chain
			smbl.utils.Rule(
				input=[
						self.full_chain_fn(iteration),
					],
				output=[
						self.full_inverted_chain_fn(iteration),
					],
				run=functools.partial(self.create_full_inverted_chain,iteration=iteration),
			)

			# lift alignments
			smbl.utils.Rule(
				input=[
						self.basic_chain_fn(iteration-1) if iteration>0 else self.unsorted_bam_fn(iteration),
						self.unsorted_bam_fn(iteration),
					],
				output=[
						self.rnf_lifted_bam_fn(iteration),
					],
				run=functools.partial(self.rnf_lift,iteration=iteration),
			)

	###########

	def create_reads(self, iteration):
		self.info_msg(iteration)
		self.reads_object.create_fastq_iteration(
				fastq_fn=self.fastq_fn(iteration),
				iteration=iteration,
			)

	def map_reads(self, iteration):
		self.info_msg(iteration)
		self.mapping_object.map_reads(
				fasta_fn=self.fasta_fn(iteration),
				fastq_fn=self.fastq_fn(iteration),
				unsorted_bam_fn=self.unsorted_bam_fn(iteration),
			)
		if not self.remapping and iteration>0:
			orig_bam=self.unsorted_bam_fn(iteration)
			prev_bam=self.unsorted_bam_fn(iteration-1)
			tmp_bam=self.unsorted_bam_fn(iteration)+".tmp"
			shutil.move(orig_bam, tmp_bam)
			smbl.utils.shell(
					"""
						"{SAMTOOLS}" merge "{orig_bam}" \
							"{previous_bam}"\
							"{tmp_bam}"\
					""".format(
							SAMTOOLS=smbl.prog.SAMTOOLS,
							orig_bam=orig_bam,
							previous_bam=prev_bam,
							tmp_bam=tmp_bam,
						)
				)

	def sort_bam(self, iteration):
		self.info_msg(iteration)
		self.sorting_object.sort_bam(self.unsorted_bam_fn(iteration),self.sorted_bam_fn(iteration));

	def create_pileup(self,iteration):
		self.info_msg(iteration)
		self.pileup_object.create_pileup(
				fasta_fn=self.fasta_fn(iteration),
				unsorted_bam_fn=self.unsorted_bam_fn(iteration),
				sorted_bam_fn=self.sorted_bam_fn(iteration),
				pileup_fn=self.pileup_fn(iteration),
			)

	def create_consensus(self, iteration):
		self.info_msg(iteration)
		self.consensus_object.create_consensus(
				fasta_fn=self.fasta_fn(iteration),
				unsorted_bam_fn=self.unsorted_bam_fn(iteration),
				sorted_bam_fn=self.sorted_bam_fn(iteration),
				pileup_fn=self.pileup_fn(iteration),
				compressed_vcf_fn=self.compressed_vcf_fn(iteration),
				iteration=iteration,
				tmp_dir=self.tmp_dir(),
			)

	def create_full_chain(self, iteration):
		self.info_msg(iteration)
		if iteration==0:
			shutil.copyfile(
					self.basic_chain_fn(0),
					self.full_chain_fn(0)
				)
		else:
			chainer=Chain_Chainer(
					chain1_fn=self.full_chain_fn(iteration-1),
					chain2_fn=self.basic_chain_fn(iteration),
					new_chain_fn=self.full_chain_fn(iteration),
				)

	def create_full_inverted_chain(self, iteration):
		self.info_msg(iteration)
		Chain.invert_chain(
				chain1_fn=self.full_chain_fn(iteration),
				chain2_fn=self.full_inverted_chain_fn(iteration),
			)

	def update_reference(self,iteration):
		self.info_msg(iteration)
		smbl.utils.shell('mkdir -p "{chain_dir}"'.format(
				chain_dir=os.path.dirname(self.basic_chain_fn(iteration))
			)
		)

		empty=True

		with gzip.open(self.compressed_vcf_fn(iteration),"r") as vcf_fo:
			for line in vcf_fo:
				line=line.decode("ascii").strip()
				if line!="" and line[0]!="#":
					empty=False
					break

		if empty:
			#FAI => chain
			shutil.copyfile(self.fasta_fn(iteration),self.fasta_fn(iteration+1))
			with open(self.basic_chain_fn(iteration),"w+") as chain_fo:
				with open(self.fasta_fn(iteration)+".fai") as fai_fo:
					for (i,line) in enumerate(fai_fo):
						line=line.strip()
						if line!="":
							(chrom,length,_,_,_)=line.split("\t")
							chain_fo.write(
									os.linesep.join(
											[
												" ".join(["chain", "0",
														chrom, length, "+", "0", length,
														chrom, length, "+", "0", length,
														"0",
													]),
												"{}".format(length),
												"",
											]
										)
								)


		else:

			smbl.utils.shell(
					"""
						"{BCFTOOLS}" consensus \
						-c "{chain_fn}" \
						-f "{old_fasta_fn}" \
						"{compressed_vcf_fn}" \
						> "{new_fasta_fn}" \
					""".format(
							BCFTOOLS=smbl.prog.BCFTOOLS,
							old_fasta_fn=self.fasta_fn(iteration),
							new_fasta_fn=self.fasta_fn(iteration+1),
							compressed_vcf_fn=self.compressed_vcf_fn(iteration),
							chain_fn=self.basic_chain_fn(iteration),
						)
				)

	def rnf_lift(self, iteration):
		self.info_msg(iteration)
		#if iteration==0:
		#	shutil.copyfile(
		#			self.unsorted_bam_fn(0),
		#			self.rnf_lifted_bam_fn(0),
		#		)
		#else:
		smbl.utils.shell(
				('"{SAMTOOLS}" view -h "{in_bam}" '
				+ ' | "{FILTER_ALIGNMENTS}" -i 13 - -'
				+ " ".join(
						[
							""" | \
								rnftools liftover \
									--faidx "{faidx}" \
									--chain "{chain}" \
									--genome-id 1 \
									-\
									-\
							""".format(
									faidx=self.fasta_fn(i)+".fai",
									chain=self.basic_chain_fn(i),
								)
							for i in range(iteration)
						]
					)
				+ ' > "{out_bam}"').format(
							FILTER_ALIGNMENTS=os.path.join(os.path.dirname(__file__),'filter_aligned_rnf_reads.py'),
							SAMTOOLS=smbl.prog.SAMTOOLS,
							in_bam=self.unsorted_bam_fn(iteration),
							out_bam=self.rnf_lifted_bam_fn(iteration),
						)
			)
