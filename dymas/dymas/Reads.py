import abc

class Reads:

	__metaclass__=abc.ABCmeta

	def __init(self,
				fastq_1_fn,
				reads_per_iteration,
				iterations=None,
				fastq_2_fn=None,
			):
		with open(fq1) as f:
			for i, l in enumerate(f):
				pass
		self.reads=(i+1)//4

		if iterations is not None:
			self.iterations=iterations
		else:
			self.reads_per_iteration=reads_per_iteration

		self.fastq_1_fn=fastq_1_fn
		self.fastq_2_fn=fastq_2_fn
	

	## Reads.reads

	@property
	def reads(self):
	    return self._reads

	@reads.setter
	def reads(self,value):
		assert value>0
		self._reads=value


	## Reads.reads_per_iteration

	@property
	def reads_per_iteration(self):
		return self._reads_per_iteration

	@reads_per_iteration.setter
	def reads_per_iteration(self,value):
		assert reads_per_iteration>0
		self._reads_per_iteration=value
		self._iterations=(self.reads+value-1)//value


	## Reads.iterations

	@property
	def iterations(self):
		return self._iterations

	@iterations.setter
	def iterations(self,value):
		assert value>0
		self._iterations=value
		self._reads_per_iteration=(self.reads+value-1)//value


	####################################

	@abc.abstractmethods
	def create_fastq_iteration(self,fastq_fn,iteration):
		return
