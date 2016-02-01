import smbl
import os

from .Consensus import Consensus

class Consensus_Ococo(Consensus):


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

		old_stats_line = ("-s " + os.path.join(tmp_dir,"stats_{}.ococo".format(iteration))) if iteration>0 else ""

		smbl.utils.shell(
				"""
				"{OCOCO}" \
					-m batch \
					-t stochastic \
					-i "{unsorted_bam_fn}" \
					-f "{fasta_fn}" \
					{old_stats_line} \
					-S "{new_stats_fn}" \
					-v - \
				| \
				"{BGZIP}" -c > "{compressed_vcf_fn}" \
				""".format(
						BGZIP=smbl.prog.BGZIP,
						OCOCO="ococo",
						unsorted_bam_fn=unsorted_bam_fn,
						old_stats_line=old_stats_line,
						new_stats_fn=os.path.join(tmp_dir,"stats_{}.ococo".format(iteration+1)),
						fasta_fn=fasta_fn,
						pileup_fn=pileup_fn,
						compressed_vcf_fn=compressed_vcf_fn,
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
