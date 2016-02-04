import smbl
import os

from .Pileup import Pileup

class Pileup_SamTools(Pileup):

	def __init__(self,
				min_mq=1,
				min_bq=13,
			):
		self.min_mq=min_mq
		self.min_bq=min_bq

	@property
	def required(self):
		return [smbl.prog.SAMTOOLS]

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn,
			):

		filter_pileup_fn=os.path.join(os.path.dirname(__file__),'filter_pileup.pl')

		smbl.utils.shell(
				"""
					"{SAMTOOLS}" mpileup\
						--min-MQ {min_mq} \
						--min-BQ {min_bq} \
						--fasta-ref "{fasta_fn}" \
						"{sorted_bam_fn}" \
					| \
					"{FILTER_PILEUP}" \
						{possible_gziping} \
						> "{pileup_fn}" \
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						FILTER_PILEUP=filter_pileup_fn,
						sorted_bam_fn=sorted_bam_fn,
						pileup_fn=pileup_fn,
						fasta_fn=fasta_fn,
						min_mq=self.min_mq,
						min_bq=self.min_bq,
						possible_gziping=" | gzip " if pileup_fn[-3:]==".gz" else "",
					)
			)
