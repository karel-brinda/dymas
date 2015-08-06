from .Reads import Reads

class Reads_Dyn(Reads):

	def __init__(self,**kwds):

		print(str(kwds))
		super().__init__(**kwds)        


	def create_fastq_iteration(self,fastq_fn,iteration):
		with open(self.fastq_1_fn) as inp:
			with open(fastq_fn,"w+") as outp:
				for i in range(self.reads_per_iteration*iteration*4):
					_ = inp.readline()
				for i in range(self.reads_per_iteration*4):
					outp.write(inp.readline())
