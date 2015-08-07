import smbl
import os

from .Consensus import Consensus

class Consensus_SamTools(Consensus):

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn
			):

		filter_pileup_fn=os.path.join(os.path.dirname(__file__),'filter_pileup.pl')

		#regexp=r"\(\.\|,\|\^.\|\$\)*",
		smbl.utils.shell(
				"""
					{SAMTOOLS} mpileup\
						--min-MQ 1 \
						--fasta-ref "{fasta_fn}" \
						"{sorted_bam_fn}" |\
						"{filter_pileup_fn}" {possible_gzip} >\
						"{pileup_fn}" \
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						sorted_bam_fn=sorted_bam_fn,
						pileup_fn=pileup_fn,
						fasta_fn=fasta_fn,
						filter_pileup_fn=filter_pileup_fn,
						possible_gzip=" | gzip " if pileup_fn[-3:]==".gz" else "",
					)
			)

	def create_compressed_vcf(self,
				fasta_fn,
				pileup_fn,
				compressed_vcf_fn,
			):

		smbl.utils.shell(
				"""
				{cat} "{pileup_fn}" | \
				{callvariants} \
					--calling-alg parikh \
					--reference "{fasta_fn}" \
					--min-coverage 2 \
					--min-base-qual 0 \
					--accept-level 0.6 \
					| \
				"{BGZIP}" -c > "{compressed_vcf_fn}" \
				""".format(
						BGZIP=smbl.prog.BGZIP,
						callvariants="call_variants",
						fasta_fn=fasta_fn,
						pileup_fn=pileup_fn,
						compressed_vcf_fn=compressed_vcf_fn,
						cat="gzcat " if pileup_fn[-3:]==".gz" else "cat",
					)
			)
		
		smbl.utils.shell(
				"""
				"{TABIX}" "{compressed_vcf_fn}"
				""".format(
						TABIX=smbl.prog.TABIX,
						compressed_vcf_fn=compressed_vcf_fn,
					)
			)
