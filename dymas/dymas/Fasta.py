from Bio import SeqIO

class Fasta:

	@staticmethod
	def load_fasta_dict(fasta_fn):
		sequences={}
		_fasta_sequences = SeqIO.parse(open(fasta_fn),'fasta')
		for seq in _fasta_sequences:
			sequences[seq.name]=seq.seq
		return sequences
