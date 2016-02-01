import smbl

from .Sorting import Sorting

class Sorting_SamTools(Sorting):

	def required(self):
		return smbl.prog.SAMTOOLS

	def sort_bam(self,
				unsorted_bam_fn,
				sorted_bam_fn,
			):
		smbl.utils.shell(
				"""
					"{SAMTOOLS}" sort \
						-l 5 \
						-@ 3 \
						-O bam \
						-T {prefix} \
						"{unsorted_bam_fn}" \
						> "{sorted_bam_fn}" \
				""".format(
						SAMTOOLS=smbl.prog.SAMTOOLS,
						unsorted_bam_fn=unsorted_bam_fn,
						sorted_bam_fn=sorted_bam_fn,
						prefix=unsorted_bam_fn+".tmp",
					)
			)
