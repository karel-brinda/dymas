import abc
import smbl

class Consensus(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self,
			):
		pass

	@property
	def required(self):
		return [
				smbl.prog.SAMTOOLS,
				smbl.prog.BCFTOOLS,
				smbl.prog.BGZIP,
				smbl.prog.TABIX,
			]

	@abc.abstractmethod
	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
			):
		return ""

	@abc.abstractmethod
	def create_vcf(self,
				fasta_fn,
				pileup_fn,
				vcf_fn,
			):
		return ""