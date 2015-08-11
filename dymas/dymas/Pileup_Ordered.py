import smbl
import os
import gzip
import pysam
import Bio

from .Pileup import Pileup
from Bio import SeqIO

class Pileup_Ordered(Pileup):

	@property
	def required(self):
		return [smbl.prog.SAMTOOLS]

	def create_pileup(self,
				fasta_fn,
				unsorted_bam_fn,
				sorted_bam_fn,
				pileup_fn
			):

		bamfile = pysam.AlignmentFile(sorted_bam_fn, "rb")

		sequences = dymas.load_fasta_dict(fasta_fn)

		with gzip.open(pileup_fn, 'w+') as f:
			for chromosome in bamfile.references:
				for column in bamfile.pileup(chromosome):
					report=False
					base=sequences[chromosome][column.pos]
					out=[]
					blocks=[]
					for read in column.pileups:
						read_name=read.alignment.query_name.split("__")
						if not read.is_del and not read.is_refskip:
							new_base=read.alignment.query_sequence[read.query_position]
							if new_base==base:
								blocks.append([read_name,"."])
							else:
								report=True
								blocks.append([read_name,new_base])
						else:
							out.append([read_name,"*"])
							report=True
					sorted(blocks,key=lambda x:x[0])
					if report:
						pileup_line="{chrom}\t{pos}\t{base}\t{cov}\t{pile}\t.{end}".format(
									chrom=chromosome,
									pos=column.pos+1,
									base=base,
									cov=len(blocks),
									pile="".join(x[1] for x in blocks),
									end=os.linesep,
								)
						f.write(bytes(pileup_line, 'UTF-8'))
