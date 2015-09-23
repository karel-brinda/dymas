from .Reads import Reads
import shutil

class Reads_ItRef(Reads):

	def __init__(self,
				fastq_1_fn,
				coverage,
				iterations,
				fastq_2_fn=None,
			):

		super().__init__(
				fastq_1_fn=fastq_1_fn,
				fastq_2_fn=fastq_2_fn,
				coverage=coverage,
			)

		self.coverage_per_iteration=coverage
		self.iterations=iterations
		self.reads_per_iteration=self.reads

	def create_fastq_iteration(self,fastq_fn,iteration):
		shutil.copyfile(self.fastq_1_fn,fastq_fn)
