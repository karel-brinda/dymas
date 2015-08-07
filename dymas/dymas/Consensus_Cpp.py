import smbl
import os

from .Consensus import Consensus

class Consensus_Cpp(Consensus):

	@property
	def required(self):
		return [
				smbl.prog.BCFTOOLS,
				smbl.prog.BGZIP,
				smbl.prog.TABIX,
			]

	def create_consensus(self,
				fasta_fn,
				pileup_fn,
				compressed_vcf_fn,
			):

		smbl.utils.shell(
				"""
				{CAT} "{pileup_fn}" \
				| \
				{CALLVARIANTS} \
					--calling-alg parikh \
					--reference "{fasta_fn}" \
					--min-coverage 2 \
					--min-base-qual 0 \
					--accept-level 0.6 \
				| \
				"{BGZIP}" -c > "{compressed_vcf_fn}" \
				""".format(
						CAT="gzcat " if pileup_fn[-3:]==".gz" else "cat",
						BGZIP=smbl.prog.BGZIP,
						CALLVARIANTS="call_variants",
						fasta_fn=fasta_fn,
						pileup_fn=pileup_fn,
						compressed_vcf_fn=compressed_vcf_fn,
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
