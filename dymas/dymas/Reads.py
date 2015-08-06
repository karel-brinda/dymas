import abc

class Reads:

	__metaclass__=abc.ABCMeta

	def __init__(self,
				reads,
				fastq_1_fn,
				reads_per_iteration=None,
				iterations=None,
				fastq_2_fn=None,
			):

		assert iterations is not None or reads_per_iteration is not None
		assert reads>0

		self.reads=reads

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

	## Reads.required

	@property
	def required(self):
		print("Reads require",self.fastq_1_fn)
		if self.fastq_2_fn is None:
			return [
					self.fastq_1_fn,
				]
		else:
			return [
					self.fastq_1_fn,
					self.fastq_2_fn ,
				]



	####################################

	@abc.abstractmethod
	def create_fastq_iteration(self,fastq_fn,iteration):
		return

