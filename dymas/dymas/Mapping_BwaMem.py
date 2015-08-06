import smbl
import snakemake

from .Mapping import Mapping

class Mapping_BwaMem(Mapping):

	def __init__(self):
		pass

	@property
	def required(self):
		return [
				smbl.prog.BWA,
				smbl.prog.SAMTOOLS,
			]

	@abc.abstractmethod
	def map_reads(self,
				fasta_fn,
				fastq_fn,
				unsorted_bam_fn,
			):

		snakemake.shell(
				"""
					"{BWA}" index "{fasta_fn}"
				""".format(
						BWA=smbl.prog.BWA,
						fasta_fn=fasta_fn,
					)
			)

		snakemake.shell(
				"""
					"{BWA}" mem "{fasta_fn}" "{fastq_fn}" |
					{SAMTOOLS} view -b - > "{unsorted_bam_fn}
				""".format(
						BWA=smbl.prog.BWA,
						SAMTOOLS=smbl.prog.SAMTOOLS,
						fasta_fn=fasta_fn,
						fastq_fn=fastq_fn,
						unsorted_bam_fn=unsorted_bam_fn,
					)
			)