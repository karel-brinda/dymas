import os
import smbl
import snakemake
import functools

class Experiment:

	def __init__(self,
				experiment_name,
				starting_reference_fasta_fn,
				mapping_object,
				reads_object,
				consensus_object,
			):

		self.experiment_name=experiment_name

		self.starting_reference_fasta_fn=starting_reference_fasta_fn
		self.mapping_object=mapping_object
		self.reads_object=reads_object
		self.consensus_object=consensus_object

	@property
	def iterations(self):
	    return self.reads_object.iterations
	
	@staticmethod
	def _iteration(iteration,suffix=""):
		return "{}{{}}".format(iteration).zfill(5).format(suffix)

	###########

	def fasta_fn(self,iteration):
		return os.path.join(experiment_name,"reference",self._iteration(iteration,".fa"))

	def fastq_fn(self,iteration):
		return os.path.join(experiment_name,"reads",self._iteration(iteration,".fq"))

	def unsorted_bam_fn(self,iteration):
		return os.path.join(experiment_name,"unsorted_bam",self._iteration(iteration,".bam"))

	def sorted_bam_fn(self,iteration):
		return os.path.join(experiment_name,"sorted_bam",self._iteration(iteration,".bam"))

	def converted_bam_fn(self,iteration):
		return os.path.join(experiment_name,"converted_bam",self._iteration(iteration,".bam"))

	def chain_fn(self,iteration):
		return os.path.join(experiment_name,"chain",self._iteration(iteration,".chain"))

	def full_inverted_chain_fn(self,iteration):
		return os.path.join(experiment_name,"full_inverted_chain",self._iteration(iteration,".chain"))

	###########

	def register_smbl_rules(self):
		for iteration in range(self.iterations):

			# create_reads
			smbl.utils.Rule(
				input=self.reads_object.fastq_1_fn,
				output=self.fastq_fn(iteration),
				run=functools.partial(self.create_reads,iteration=iteration),
			)

			# map_reads
			smbl.utils.Rule(
				input=[self.fasta_fn(iteration),self.fastq_fn(iteration)],
				output=self.unsorted_bam_fn(iteration),
				run=functools.partial(self.map_reads,iteration=iteration),
			)

			# sort_bam
			smbl.utils.Rule(
				input=self.unsorted_bam_fn(iteration),
				output=self.sorted_bam_fn(iteration),
				run=functools.partial(self.sort_bam,iteration=iteration),
			)

			# call_consensus
			smbl.utils.Rule(
				input=self.sorted_bam_fn,
				output=self.fasta_fn(iteration+1),
				run=functools.partial(self.consensus_object.call_consensus,iteration=iteration),
			)

	###########

	def create_reads(self, iteration):
		self.reads_object.create_fastq_iteration(
				fastq_fn=self.fastq_fn(iteration),
				iteration=iteration,
			)

	def map_reads(self, iteration):
		self.mapping_object.map_reads(
				fasta_fn=self.fasta_fn(iteration),
				fastq_fn=self.fastq_fn(iteration),
				unsorted_bam_fn=self.unsorted_bam_fn(iteration),
			)

	def sort_bam(self, iteration):
		snakemake.shell(
				"""
					"{SAMTOOLS}" sort \
						-l 5 \
						-@ 3 \
						"{unsorted_bam_fn}" \
						> "{sorted_bam_fn}" \
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						unsorted_bam_fn=self.unsorted_bam_fn(iteration),
						sorted_bam_fn=self.sorted_bam_fn(iteration),
					)
			)

	def call_consensus(self, iteration):
		self.consensus_object.call_consensus(
				old_fasta_fn=self.fasta_fn(iteration),
				new_fasta_fn=self.fasta_fn(iteration+1),
				sorted_bam_fn=self.sorted_bam_fn(iteration),
			)

	def lift_alignments(self, iteration):
		pass
