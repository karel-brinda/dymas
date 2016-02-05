import smbl
import os

from .Consensus import Consensus

class Consensus_Ococo(Consensus):

	def __init__(self,
				strategy="majority",
				min_mq=1,
				min_bq=13,
				variant=16,
				ref_weight=0,
				min_coverage=2,
			):
		assert variant in [16,32], "Wrong variant ({}).".format(variant)

		self.strategy=strategy
		self.min_mq=min_mq
		self.min_bq=min_bq
		self.variant=variant
		self.ref_weight=ref_weight
		self.min_coverage=min_coverage

	@property
	def required(self):
		return [
				smbl.prog.BGZIP,
				smbl.prog.TABIX,
			]

	def create_consensus(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn,
				compressed_vcf_fn,
				tmp_dir,
				iteration,
			):

		os.makedirs(tmp_dir,exist_ok=True)

		if iteration==0:
			in_fasta_line = '-f "{}"'.format(fasta_fn)
			old_stats_line = ""
		else:
			in_fasta_line=""
			old_stats_line = '-s "{}"'.format(os.path.join(tmp_dir,"stats_{}.ococo".format(iteration)))
		
		smbl.utils.shell(
				"""
				"{OCOCO}" \
					-i "{unsorted_bam_fn}" \
					{in_fasta_line} \
					{old_stats_line} \
					-S "{new_stats_fn}" \
					--min-MQ {min_mq} \
					--min-BQ {min_bq} \
					--ref-weight {ref_weight} \
					--min-coverage {min_coverage} \
					--strategy {strategy} \
					--mode batch \
					-v - \
				| \
				"{BGZIP}" -c > "{compressed_vcf_fn}" \
				""".format(
						BGZIP=smbl.prog.BGZIP,
						OCOCO="ococo" if self.variant==16 else "ococo32",
						unsorted_bam_fn=unsorted_bam_fn,
						old_stats_line=old_stats_line,
						new_stats_fn=os.path.join(tmp_dir,"stats_{}.ococo".format(iteration+1)),
						in_fasta_line=in_fasta_line,
						pileup_fn=pileup_fn,
						compressed_vcf_fn=compressed_vcf_fn,
						strategy=self.strategy,
						min_mq=self.min_mq,
						min_bq=self.min_bq,
						ref_weight=self.ref_weight,
						min_coverage=self.min_coverage,
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
