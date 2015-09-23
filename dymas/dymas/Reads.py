import abc

class Reads:

	__metaclass__=abc.ABCMeta

	def __init__(self,
				fastq_1_fn,
				coverage,
				fastq_2_fn=None,
			):

		with open(fastq_1_fn) as fastq_1_fo:
			for (i,line) in enumerate(fastq_1_fo):
				if i==2:
					self.read_length=len(line.strip())

			self.reads=i//4

		self.fastq_1_fn=fastq_1_fn
		self.fastq_2_fn=fastq_2_fn

		self.coverage=coverage
	
	## Reads.reads

	@property
	def reads(self):
	    return self._reads

	@reads.setter
	def reads(self,value):
		assert value>0
		self._reads=value


	## Reads.coverage

	@property
	def coverage(self):
		return self._coverage

	@coverage.setter
	def coverage(self,value):
		assert value>0
		self._coverage=value

	## Reads.coverage_per_iteration

	@property
	def coverage_per_iteration(self):
		return self._coverage_per_iteration

	@coverage_per_iteration.setter
	def coverage_per_iteration(self,value):
		assert value>0
		self._reads_per_iterationn=value

	## Reads.reads_per_iteration

	@property
	def reads_per_iteration(self):
		return self._reads_per_iteration

	@reads_per_iteration.setter
	def reads_per_iteration(self,value):
		assert value>0
		self._reads_per_iteration=value

	## Reads.iterations

	@property
	def iterations(self):
		return self._iterations

	@iterations.setter
	def iterations(self,value):
		assert value>0
		self._iterations=value

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

