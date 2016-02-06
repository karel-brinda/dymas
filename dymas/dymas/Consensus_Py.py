import smbl
import os
import numpy
import gzip

from .Consensus import Consensus
from .Vcf import Vcf

class Consensus_Py(Consensus):

	def __init__(self,
				min_coverage=2,
				accept_level=0.6,
				call_snps=True,
				call_ins=True,
				call_dels=True,
				keep_del_stats=False,
			):

		self.min_coverage=min_coverage
		self.accept_level=accept_level
		self.call_snps=call_snps
		self.call_ins=call_ins
		self.call_dels=call_dels
		self.keep_del_stats=keep_del_stats


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
				**kwargs
			):

		vcf_fn=compressed_vcf_fn[:-3]

		vcf=Vcf(
				vcf_fn=vcf_fn,
				fasta_fn=fasta_fn,
			)

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

			for line in f:

				(chrom, pos, base, cov, nucls, _) = line.split("\t")

				trans["."]=trans[","]=trans[base]
				vector_snps = numpy.array([0, 0, 0, 0, 0])
				vector_ins = numpy.array([0, 0, 0, 0])

				# filling vector_snps and vector_ins
				cov=int(cov)
				i=0
				l=len(nucls)
				while i<l:
					try:
						char=nucls[i]
						vector_snps[trans[char]]+=1
						i+=1
					except:
						if char=="+" or char=="-":
							k=i+1
							while nucls[k] in "0123456789" and k<l:
								k+=1
							number=int(nucls[i+1:k])
							i=k+number

							if char=="+":
								inserted_nucls=nucls[k:k+number]
								for char in set(list(inserted_nucls)):
									vector_ins[trans[char]]+=1

						elif char=="^":
							i+=2
						elif char in "$<>":
							i+=1
						else:
							raise NotImplementedError("Unknown character '{}'".format(char))

				if self.call_dels or self.keep_del_stats:
					cov_2=vector_snps[0]+vector_snps[1]+vector_snps[2]+vector_snps[3]+vector_snps[4]
				else:
					cov_2=vector_snps[0]+vector_snps[1]+vector_snps[2]+vector_snps[3]

				if cov_2<self.min_coverage:
					continue

				for i in range(5):
					if vector_snps[i]>=self.accept_level*cov_2:
						# calling deletions
						if i==4:
							if self.call_dels:
								vcf.add_del(
										chromosome=chrom,
										position=int(pos),
									)
						# calling snps
						else:
							if self.call_snps:
								new_base=trans_inv[i]
								# debugging (want to have 1 snp / line)
								call_some_indels = self.call_dels or self.call_ins
								if base != new_base:
									vcf.add_snp(
											chromosome=chrom,
											position=int(pos),
											new_base=new_base,
											flush_immediately=not call_some_indels,
										)
						break

				# calling insertions
				if self.call_ins:
					max_votes_ins=max(vector_ins)
					if max_votes_ins>=self.accept_level*cov:
						for i in range(4):
							if vector_ins[i]==max_votes_ins:
								vcf.add_ins(
										chromosome=chrom,
										position=int(pos),
										new_base=trans_inv[i],
									)
								break

		#to flush buffer
		del vcf

		smbl.utils.shell(
				"""
				"{BGZIP}" -f "{vcf_fn}"
				""".format(
						BGZIP=smbl.prog.BGZIP,
						vcf_fn=vcf_fn,
					)
			)

		smbl.utils.shell(
				"""
				"{TABIX}" -f "{compressed_vcf_fn}"
				""".format(
						TABIX=smbl.prog.TABIX,
						compressed_vcf_fn=compressed_vcf_fn,
					)
			)
