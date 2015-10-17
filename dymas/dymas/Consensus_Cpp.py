import smbl
import os

from .Consensus import Consensus

class Consensus_Cpp(Consensus):

	def __init__(self,
				min_coverage=2,
				min_base_qual=0,
				accept_level=0.6,
			):

		self.min_coverage=min_coverage
		self.min_base_qual=min_base_qual
		self.accept_level=accept_level


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
				{CALLCONSENSUS} \
					--calling-alg parikh \
					--reference "{fasta_fn}" \
					--min-coverage {min_coverage} \
					--min-base-qual {min_base_qual} \
					--accept-level {accept_level} \
				| \
				"{BGZIP}" -c > "{compressed_vcf_fn}" \
				""".format(
						CAT="gzcat " if pileup_fn[-3:]==".gz" else "cat",
						BGZIP=smbl.prog.BGZIP,
						CALLCONSENSUS=os.path.relpath(
								os.path.join(
									os.path.dirname(__file__),
									"..",
									"..",
									"misc",
									"call_consensus_cpp",
									"call_consensus",
								),
								os.path.dirname(__file__),
							),
						fasta_fn=fasta_fn,
						pileup_fn=pileup_fn,
						compressed_vcf_fn=compressed_vcf_fn,
						min_coverage=self.min_coverage,
						min_base_qual=self.min_base_qual,
						accept_level=self.accept_level,
					)
			)

		smbl.utils.shell(
				"""
				"{TABIX}" -f "{compressed_vcf_fn}"
				""".format(
						TABIX=smbl.prog.TABIX,
						compressed_vcf_fn=compressed_vcf_fn,
					)
			)
