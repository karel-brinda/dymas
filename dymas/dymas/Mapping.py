
class Mapping:

	__metaclass__ = abc.ABCmeta

	def __init__(self):
		pass

	@property
	def required(self):
		return []

	@abc.abstractmethod
	def map_reads(self,
				fasta_fn,
				fastq_fn,
				unsorted_bam_fn,
			):
		return ""
