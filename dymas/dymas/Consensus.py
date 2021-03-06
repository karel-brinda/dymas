import abc
import smbl

class Consensus(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self,
			):
		pass

	@abc.abstractproperty
	def required(self):
		return

	@abc.abstractmethod
	def create_consensus(self,
				fasta_fn,
				pileup_fn,
				compressed_vcf_fn,
			):
		return
