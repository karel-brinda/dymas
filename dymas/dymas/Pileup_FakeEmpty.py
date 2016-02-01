from .Pileup import Pileup

class Pileup_FakeEmpty(Pileup):

	@property
	def required(self):
		return []

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn
			):

		with open(pileup_fn,"w+") as f:
			pass
