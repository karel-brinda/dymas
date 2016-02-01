import abc

class Sorting(object):

	__metaclass__ = abc.ABCMeta

	def __init__(self,
			):
		pass

	@abc.abstractproperty
	def required(self):
		return

	@abc.abstractmethod
	def sort_bam(self,
				unsorted_bam_fn,
				sorted_bam_fn,
			):
		return
