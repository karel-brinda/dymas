import abc

class Consensus(object):

	__metaclass__ = abc.ABCmeta

	def __init__(self,
				a,
			):
		pass

	@abc.abstractmethod
	def call_consensus(
				old_fasta_fn,
				new_fasta_fn,
				sorted_bam_fn,
			):
		return ""