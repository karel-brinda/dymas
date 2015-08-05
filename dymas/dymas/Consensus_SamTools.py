import smbl
import snakemake

from .Consensus import Consensus

class Consensus_SamTools(Consensus):

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
			):
		return ""

	def create_vcf(self,
				fasta_fn,
				pileup_fn,
				vcf_fn,
			):
		return ""