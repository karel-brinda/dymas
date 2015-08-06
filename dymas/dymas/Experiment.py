import os
import smbl
import functools
import shutil

# todo: tabix

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

		self.register_smbl_rules()

	def input(self):
		return [
				self.fasta_fn(self.iterations)
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
		return os.path.join(self.experiment_name,"3_unsorted_bam",self._iteration(iteration,".bam"))

	def sorted_bam_fn(self,iteration):
		return os.path.join(self.experiment_name,"4_sorted_bam",self._iteration(iteration,".bam"))

	def converted_bam_fn(self,iteration):
		return os.path.join(self.experiment_name,"5_converted_bam",self._iteration(iteration,".bam"))

	def pileup_fn(self,iteration):
		return os.path.join(self.experiment_name,"6_pileup",self._iteration(iteration,".pileup"))

	def vcf_fn(self,iteration):
		return os.path.join(self.experiment_name,"7_vcf",self._iteration(iteration,".vcf"))

	def bcf_fn(self,iteration):
		return os.path.join(self.experiment_name,"7_vcf",self._iteration(iteration,".vcf.gz"))

	def chain_fn(self,iteration):
		return os.path.join(self.experiment_name,"8_chain",self._iteration(iteration,".chain"))

	def full_inverted_chain_fn(self,iteration):
		return os.path.join(self.experiment_name,"9_full_inverted_chain",self._iteration(iteration,".chain"))

	###########

	def register_smbl_rules(self):
		smbl.utils.Rule(
				input=self.starting_reference_fasta_fn,
				output=self.fasta_fn(0),
				run=lambda: shutil.copyfile(self.starting_reference_fasta_fn,self.fasta_fn(0)),
			)


		for iteration in range(self.iterations):

			# create_reads
			smbl.utils.Rule(
				input=[
						self.reads_object.required
					],
				output=self.fastq_fn(iteration),
				run=functools.partial(self.create_reads,iteration=iteration),
			)

			# map_reads
			smbl.utils.Rule(
				input=[
						self.fasta_fn(iteration),
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
						self.consensus_object.required,
						self.fasta_fn(iteration),
						self.unsorted_bam_fn(iteration),
						self.sorted_bam_fn(iteration),
					],
				output=self.pileup_fn(iteration),
				run=functools.partial(self.create_pileup,iteration=iteration),
			)

			# create_vcf
			smbl.utils.Rule(
				input=[
						self.consensus_object.required,
						self.fasta_fn(iteration),
						self.pileup_fn(iteration),
					],
				output=[
						self.vcf_fn(iteration),
						self.bcf_fn(iteration),
					],
				run=functools.partial(self.create_vcf,iteration=iteration),
			)

			# update_reference
			smbl.utils.Rule(
				input=[
						self.consensus_object.required,
						self.fasta_fn(iteration),
						self.fasta_fn(iteration)+".fai",
						self.vcf_fn(iteration),
					],
				output=self.fasta_fn(iteration+1),
				run=functools.partial(self.update_reference,iteration=iteration),
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
		smbl.utils.shell(
				"""
					"{SAMTOOLS}" sort \
						-l 5 \
						-@ 3 \
						-O bam \
						-T {prefix} \
						"{unsorted_bam_fn}" \
						> "{sorted_bam_fn}" \
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						unsorted_bam_fn=self.unsorted_bam_fn(iteration),
						sorted_bam_fn=self.sorted_bam_fn(iteration),
						prefix=self.sorted_bam_fn(iteration)+".tmp",
					)
			)

	def create_pileup(self,iteration):
		self.consensus_object.create_pileup(
				fasta_fn=self.fasta_fn(iteration),				
				unsorted_bam_fn=self.unsorted_bam_fn(iteration),
				sorted_bam_fn=self.sorted_bam_fn(iteration),
				pileup_fn=self.pileup_fn(iteration),				
			)

	def create_vcf(self, iteration):
		self.consensus_object.create_vcf(
				fasta_fn=self.fasta_fn(iteration),				
				pileup_fn=self.pileup_fn(iteration),
				vcf_fn=self.vcf_fn(iteration),
			)
		self.create_bcf(iteration)

	def create_bcf(self, iteration):
		smbl.utils.shell(
				"""
					"{BGZIP}" \
					"{vcf_fn}" \
					-c > "{bcf_fn}" \
				""".format(
						BGZIP=smbl.prog.BGZIP,
						vcf_fn=self.vcf_fn(iteration),
						bcf_fn=self.bcf_fn(iteration),
					)
			)

		smbl.utils.shell(
				"""
					"{TABIX}" "{bcf_fn}"
				""".format(
						TABIX=smbl.prog.TABIX,
						bcf_fn=self.bcf_fn(iteration),
					)
			)

	def update_reference(self,iteration):
		#new_fasta_fn=self.fasta_fn(iteration+1),
		#			-c "{chain_fn}" \

		smbl.utils.shell('mkdir -p "{chain_dir}"'.format(chain_dir=os.path.dirname(self.chain_fn(iteration))))

		smbl.utils.shell(
				"""
					"{BCFTOOLS}" consensus \
					-c "{chain_fn}" \
					-f "{old_fasta_fn}" \
					"{bcf_fn}" \
					> "{new_fasta_fn}" \
				""".format(
						BCFTOOLS=smbl.prog.BCFTOOLS,
						old_fasta_fn=self.fasta_fn(iteration),
						new_fasta_fn=self.fasta_fn(iteration+1),
						bcf_fn=self.bcf_fn(iteration),
						chain_fn=self.chain_fn(iteration),
					)
			)

	def lift_alignments(self, iteration):
		pass
