import smbl
import multiprocessing

from .Mapping import Mapping

class Mapping_BwaMem(Mapping):

	def __init__(self):
		#self.cores=multiprocessing.cpu_count()
		self.cores=4

	@property
	def required(self):
		return [
				smbl.prog.BWA,
				smbl.prog.SAMTOOLS,
			]

	def map_reads(self,
				fasta_fn,
				fastq_fn,
				unsorted_bam_fn,
			):

		smbl.utils.shell(
				"""
					"{BWA}" index "{fasta_fn}"
				""".format(
						BWA=smbl.prog.BWA,
						fasta_fn=fasta_fn,
					)
			)

		smbl.utils.shell(
				"""
					"{BWA}" mem -t {cores} "{fasta_fn}" "{fastq_fn}" | \
					{SAMTOOLS} view -b - > "{unsorted_bam_fn}"
				""".format(
						BWA=smbl.prog.BWA,
						SAMTOOLS=smbl.prog.SAMTOOLS,
						fasta_fn=fasta_fn,
						fastq_fn=fastq_fn,
						unsorted_bam_fn=unsorted_bam_fn,
						cores=self.cores,
					)
			)
