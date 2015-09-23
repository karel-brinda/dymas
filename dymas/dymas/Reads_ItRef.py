from .Reads import Reads
import shutil

class Reads_ItRef(Reads):

	def __init__(self,**kwds):

		print(str(kwds))
		super().__init__(**kwds)        


	def create_fastq_iteration(self,fastq_fn,iteration):
		shutil.copyfile(self.fastq_1_fn,fastq_fn)
