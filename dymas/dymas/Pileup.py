import abc

class Pileup(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self,
			):
		pass

	@abc.abstractproperty
	def required(self):
		return

	@abc.abstractmethod
	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
			):
		return
