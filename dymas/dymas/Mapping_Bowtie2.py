import smbl
import multiprocessing

from .Mapping import Mapping

class Mapping_Bowtie2(Mapping):

	def __init__(self,local_alignment=False):
		self.cores=multiprocessing.cpu_count()
		self.local_alignment=local_alignment

	@property
	def required(self):
		return [
				smbl.prog.BOWTIE2,
				smbl.prog.BOWTIE2_BUILD,
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
						BOWTIE2BUILD=smbl.prog.BOWTIE2_BUILD,
						fasta_fn=fasta_fn,
					)
			)

		smbl.utils.shell(
				"""
					"{BOWTIE2}" -p {cores} -x "{fasta_fn}" -U "{fastq_fn}" {local} | \
					{SAMTOOLS} view -b - > "{unsorted_bam_fn}"
				""".format(
						BOWTIE2=smbl.prog.BOWTIE2,
						SAMTOOLS=smbl.prog.SAMTOOLS,
						fasta_fn=fasta_fn,
						fastq_fn=fastq_fn,
						unsorted_bam_fn=unsorted_bam_fn,
						cores=self.cores,
						local="--local" if self.local_alignment else "",
					)
			)
