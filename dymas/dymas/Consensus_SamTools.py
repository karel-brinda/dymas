import smbl

from .Consensus import Consensus

class Consensus_SamTools(Consensus):

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn
			):

		smbl.utils.shell(
				"""
					{SAMTOOLS} mpileup\
						--min-MQ 1 \
						--fasta-ref "{fasta_fn}" \
						"{sorted_bam_fn}" > \
						"{pileup_fn}"
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						sorted_bam_fn=sorted_bam_fn,
						pileup_fn=pileup_fn,
						fasta_fn=fasta_fn,
					)
			)

	def create_vcf(self,
				fasta_fn,
				pileup_fn,
				vcf_fn,
			):

		smbl.utils.shell(
				"""{callvariants} \
					--calling-alg parikh \
					--reference "{fasta_fn}" \
					--min-coverage 2 \
					--min-base-qual 0 \
					--accept-level 0.6 \
					< "{pileup_fn}" \
					> "{vcf_fn}" \
				""".format(
						callvariants="call_variants",
						fasta_fn=fasta_fn,
						pileup_fn=pileup_fn,
						vcf_fn=vcf_fn,
					)
			)
