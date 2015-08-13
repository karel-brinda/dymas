import os
from .Fasta import Fasta

class Vcf:

	# buffer example:
	#   ('chr1', 147, 'C', 'GG')
	#   ('chr1', 148, 'A', 'G')
	#   ('chr1', 149, 'A', '')

	def __init__(self,
				vcf_fn,
				fasta_fn,
			):	
		self._fasta_fn=fasta_fn
		self._fasta_dict=Fasta.load_fasta_dict(fasta_fn)

		self._vcf_fo=open(vcf_fn,"w+")
		self._vcf_fo.write(os.linesep.join(
					[
						"##fileformat=VCFv4.2",
						"##fileDate={}".format("20150000"), #FIX!!!
						"##reference={}".format(os.path.abspath(self._fasta_fn)),
						"#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO",
						"",
					]
				)
			)

		self._buffer=[]


	def __del__(self):
		self._flush()
		self._vcf_fo.close()


	@property
	def fasta_dict(self):
		return self._fasta_fn


	def add_snp(self,chromosome, position, new_base):
		self._check_chromosome_and_position(chromosome,last_useful_position=position-1)
		if len(self._buffer)>0 and self._buffer[-1][1]==position:
			#record for this position already exists => modify
			assert(len(self._buffer[-1][3])==1)
			self._buffer[-1][3]=new_base
		else:
			#record for this position does not exist yet => add
			self._buffer.append(
					[
						chromosome,
						position,
						self._fasta_dict[chromosome][position-1],
						new_base,
					]
				)

	def add_ins(self,chromosome, position, new_base):
		self._check_chromosome_and_position(chromosome,last_useful_position=position)
		if len(self._buffer)>0 and self._buffer[-1][1]==position:
			assert(len(self._buffer[-1][3])==1)
			self._buffer[-1][3]+=new_base
		else:
			self._buffer.append(
					[
						chromosome,
						position,
						self._fasta_dict[chromosome][position-1],
						self._fasta_dict[chromosome][position-1]+new_base,
					]
				)

	def add_del(self,chromosome, position):
		self._check_chromosome_and_position(chromosome,last_useful_position=position-1)
		if position==1:
			#first base => right context
			self._buffer.append(
					[
						chromosome,
						position,
						self._fasta_dict[chromosome][position-1],
						'',
					]
				)
			self._buffer.append(
					[
						chromosome,
						position+1,
						self._fasta_dict[chromosome][position],
						self._fasta_dict[chromosome][position],
					]
				)
		else:
			#non-first base => left context
			if len(self._buffer)==0:
				#left context does not exist => add
				self._buffer.append(
						[
							chromosome,
							position-1,
							self._fasta_dict[chromosome][position-2],
							self._fasta_dict[chromosome][position-2],
						]
					)
			assert(self._buffer[-1][0]==chromosome)
			assert(self._buffer[-1][1]==position-1)
			self._buffer.append(
					[
						chromosome,
						position,
						self._fasta_dict[chromosome][position-1],
						'',
					]
				)

	def _check_chromosome_and_position(self,chromosome,last_useful_position):
		if len(self._buffer)>0:
			if self._buffer[-1][0]!=chromosome or self._buffer[-1][1]<last_useful_position:
				self._flush()
		self._chrom=chromosome


	def _flush(self):
		if len(self._buffer)>0:
			if len(self._buffer)>1:
				assert set([self._buffer[i+1][1] - self._buffer[i][1] for i in range(len(self._buffer)-1)]).issubset(set([1])), str(self._buffer)
			chrom=self._buffer[0][0]
			pos=self._buffer[0][1]
			old_bases="".join([x[2] for x in self._buffer])
			new_bases="".join([x[3] for x in self._buffer if x[3] is not None])
			self._vcf_fo.write(self._vcf_line_substitution(
					chrom=chrom,
					pos=pos,
					old_bases=old_bases,
					new_bases=new_bases,
				))
			self._buffer=[]


	@staticmethod
	def _vcf_line_substitution(chrom,pos,old_bases,new_bases):
		return "{chrom}\t{pos}\t.\t{old_bases}\t{new_bases}\t100\tPASS\t.{end}".format(
											chrom=chrom,
											pos=pos,
											old_bases=old_bases,
											new_bases=new_bases,
											end=os.linesep,
										)
