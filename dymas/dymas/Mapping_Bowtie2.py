import smbl
import multiprocessing

from .Mapping import Mapping

class Mapping_Bowtie2(Mapping):

	def __init__(self):
		self.cores=multiprocessing.cpu_count()

	@property
	def required(self):
		return [
				#smbl.prog.BOWTIE2,
				smbl.prog.SAMTOOLS,
			]

	def map_reads(self,
				fasta_fn,
				fastq_fn,
				unsorted_bam_fn,
			):

		smbl.utils.shell(
				"""
					"{BOWTIE2BUILD}" "{fasta_fn}" "{fasta_fn}"
				""".format(
						BOWTIE2BUILD="bowtie2-build",
						fasta_fn=fasta_fn,
					)
			)

		smbl.utils.shell(
				"""
					"{BOWTIE2}" -p {cores} -x "{fasta_fn}" -U "{fastq_fn}" | \
					{SAMTOOLS} view -b - > "{unsorted_bam_fn}"
				""".format(
						BOWTIE2="bowtie2",
						SAMTOOLS=smbl.prog.SAMTOOLS,
						fasta_fn=fasta_fn,
						fastq_fn=fastq_fn,
						unsorted_bam_fn=unsorted_bam_fn,
						cores=self.cores,
					)
			)
