import smbl
import os

from .Pileup import Pileup

class Pileup_SamTools(Pileup):

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
						--min-MQ 1 \
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
						possible_gziping=" | gzip " if pileup_fn[-3:]==".gz" else "",
					)
			)
