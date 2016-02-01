import os

from .Sorting import Sorting

class Sorting_FakeNoSort(Sorting):

	def required(self):
		return

	def sort_bam(self,
				unsorted_bam_fn,
				sorted_bam_fn,
			):

		os.symlink("../../"+unsorted_bam_fn,sorted_bam_fn)
