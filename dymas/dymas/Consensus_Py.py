import smbl
import os
import numpy
import gzip

from .Consensus import Consensus

def vcf_line_substitution(chrom,pos,old_base,new_base):
	return "{chrom}\t{pos}\t.\t{old_base}\t{new_base}\t100\tPASS\t.{end}".format(
										chrom=chrom,
										pos=pos,
										old_base=old_base,
										new_base=new_base,
										end=os.linesep,
									)

def vcf_line_deletion(chrom,pos,base,new_base):
	pass
	#return "{chrom}\t{pos}\t.\t{old_base}\t{new_base}\t100\tPASS\t.".format(
	#									chrom=chrom,
	#									pos=pos,
	#									old_base=old_base,
	#									new_base=new_base,
	#									end=os.linesep,
	#								)


class Consensus_Py(Consensus):

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

		vcf_fn=compressed_vcf_fn[:-3]

		trans = {
				"a":0,
				"A":0,
				"C":1,
				"c":1,
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
					cov=float(cov)
					if int(cov)<3:
						continue
					trans["."]=trans[","]=trans[base]
					vector = numpy.array([0, 0, 0, 0, 0])

					i=0
					l=len(nucls)
					while i<l:
						try:
							char=nucls[i]
							vector[trans[char]]+=1
						except:
							if char=="+" or char=="-":
								k=i+1
								while nucls[k] in "0123456789" and k<l:
									k+=1
								number=int(nucls[i+1:k])
								i=k
						i+=1
					vector_norm=vector/cov
					for i in range(5):
						if vector[i]>=0.6:
							if i==5:
									g.write(vcf_line_deletion(
											chrom=chrom,
											pos=pos,
											base=base,
										))
							else:
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
				"{BGZIP}" "{vcf_fn}" \
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
