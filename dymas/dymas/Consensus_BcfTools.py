import smbl
import os
import numpy
import gzip

from .Consensus import Consensus

#
# REMARKS:
#   - pileup must have matches with "." and ","
#

class Consensus_BcfTools(Consensus):

	def __init__(self,
			):
		pass


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

		vcf_fn=compressed_vcf_fn[:-3]
		filter_bcftools_consensus_fn=os.path.join(os.path.dirname(__file__),'filter_bcftools_consensus.pl')

		# ~/.smbl/bin/bcftools call -c | ~/github/dymas/dymas/dymas/filter_bcftools_consensus.pl
		smbl.utils.shell(
				"""
				{CAT} "{pileup_fn}" \
				| \
				"{BCFTOOLS}" call -c \
				| \
				"{FILTER_BCFTOOLS_CONSENSUS}" \
				\
				> "{vcf_fn}" \
				""".format(
						CAT="gzcat" if pileup_fn[-3:]==".gz" else "cat",
						BCFTOOLS=smbl.prog.BCFTOOLS,
						FILTER_BCFTOOLS_CONSENSUS=filter_bcftools_consensus_fn,
						pileup_fn=pileup_fn,
						vcf_fn=vcf_fn,
					)
			)

		smbl.utils.shell(
				"""
				"{BGZIP}" "{vcf_fn}"
				""".format(
						BGZIP=smbl.prog.BGZIP,
						vcf_fn=vcf_fn,
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
