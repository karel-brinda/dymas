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
		#shutil.copyfile(self.fastq_1_fn,fastq_fn)

		with open(self.fastq_1_fn) as inp:
			with open(fastq_fn,"w+") as outp:
				for i,line in enumerate(inp):
					if i%4==0:
						outp.write("@itref{}".format(str(iteration).zfill(3)))
						outp.write(line[1:])
					else:
						outp.write(line)

