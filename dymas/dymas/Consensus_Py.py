import smbl
import os
import numpy
import gzip

from Bio import SeqIO

from .Consensus import Consensus

def vcf_line_substitution(chrom,pos,old_base,new_base):
	return "{chrom}\t{pos}\t.\t{old_base}\t{new_base}\t100\tPASS\t.{end}".format(
										chrom=chrom,
										pos=pos,
										old_base=old_base,
										new_base=new_base,
										end=os.linesep,
									)


class Consensus_Py(Consensus):

	def __init__(self,
				min_coverage=2,
				accept_level=0.6,
				call_snps=True,
				call_ins=True,
				call_dels=True,
			):

		self.min_coverage=min_coverage
		self.accept_level=accept_level
		self.call_snps=call_snps
		self.call_ins=call_ins
		self.call_dels=call_dels


	@property
	def required(self):
		return [
				smbl.prog.BGZIP,
				smbl.prog.TABIX,
			]

	def create_consensus(self,
				fasta_fn,
				pileup_fn,
				compressed_vcf_fn,
			):

		sequences={}
		_fasta_sequences = SeqIO.parse(open(fasta_fn),'fasta')
		for seq in _fasta_sequences:
			sequences[seq.name]=seq.seq
		_fasta_sequences = None


		vcf_fn=compressed_vcf_fn[:-3]

		trans = {
				"a":0,
				"A":0,
				"c":1,
				"C":1,
				"g":2,
				"G":2,
				"t":3,
				"T":3,
				"*":4,
			}

		trans_inv = ["A","C","G","T","*"]

		with gzip.open(pileup_fn,"tr") as f:
			with open(vcf_fn,"w+") as g:
				g.write(os.linesep.join(
						[
							"##fileformat=VCFv4.2",
							"##fileDate={}".format("20150000"), #FIX!!!s
							"##reference={}".format(os.path.abspath(fasta_fn)),
							"#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO",
							""
						]
						))

				for line in f:
					#print(line)
					(chrom, pos, base, cov, nucls, _) = line.split("\t")
					cov=int(cov)
					if int(cov)<self.min_coverage:
						continue
					trans["."]=trans[","]=trans[base]
					vector = numpy.array([0, 0, 0, 0, 0])

					i=0
					l=len(nucls)
					while i<l:
						try:
							char=nucls[i]
							vector[trans[char]]+=1
							i+=1
						except:
							if char=="+" or char=="-":
								k=i+1
								while nucls[k] in "0123456789" and k<l:
									k+=1
								number=int(nucls[i+1:k])
								inserted_nucls=nucls[k:k+number]
								i=k+number
							elif char=="^":
								i+=2
							elif char in "$<>":
								i+=1
							else:
								raise NotImplementedError("Unknown character '{}'".format(char))

					for i in range(5):
						if vector[i]>=self.accept_level*cov:
							if i==4:
								if self.call_dels:
									old_bases=sequences[chrom][int(pos)-2:int(pos)]
									g.write(vcf_line_substitution(
											chrom=chrom,
											pos=int(pos)-1,
											old_base=old_bases,
											new_base=old_bases[1],
										))
							else:
								if self.call_snps:
									new_base=trans_inv[i]
									if base != new_base:
										g.write(vcf_line_substitution(
												chrom=chrom,
												pos=pos,
												old_base=base,
												new_base=new_base,
											))
							break


		smbl.utils.shell(
				"""
				"{BGZIP}" "{vcf_fn}"
				""".format(
						BGZIP=smbl.prog.BGZIP,
						vcf_fn=vcf_fn,
					)
			)

		smbl.utils.shell(
				"""
				"{TABIX}" "{compressed_vcf_fn}"
				""".format(
						TABIX=smbl.prog.TABIX,
						compressed_vcf_fn=compressed_vcf_fn,
					)
			)
