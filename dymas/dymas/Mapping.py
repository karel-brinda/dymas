import abc

class Mapping(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self):
		pass

	@abc.abstractproperty
	def required(self):
		return

	@abc.abstractmethod
	def map_reads(self,
				fasta_fn,
				fastq_fn,
				unsorted_bam_fn,
			):
		return
