import os

from .Chain import Chain

class Chain_Chainer:

	def __init__(self,chain1_fn, chain2_fn,new_chain_fn):
		self.chain_out_fo=open(new_chain_fn,"w+")
		self.chain1=Chain(chain1_fn)
		self.chain2=Chain(chain2_fn)
		self._buffer=[]

		self.chain_out_fo.write(" ".join(
			[
				"chain",
				self.chain1.score,
				self.chain1.tName,
				self.chain1.tSize,
				self.chain1.tStrand,
				self.chain1.tStart,
				self.chain1.tEnd,
				self.chain2.qName,
				self.chain2.qSize,
				self.chain2.qStrand,
				self.chain2.qStart,
				self.chain2.qEnd,
				self.chain2.id,
			])+os.linesep
		)

		self._last_was_matching=False

		self.process()

	def __del__(self):
		self.chain_out_fo.close()

	def add_operation(self,length,operation):
		if length>0:
			if len(self._buffer)==0:
				self._buffer.append((length,operation))
			else:
				last_len=self._buffer[-1][0]
				last_op=self._buffer[-1][1]
				if last_op==operation:
					self._buffer[-1][0]+=length
				else:
					if set([last_op,operation]).issubset(set(["L","R"])):
						# L/R => removing

						m=min(last_len,length)
						del self._buffer[-1]
						self.add_operation(length-m,operation)
						self.add_operation(last_len-m,last_op)

					else:
						self._buffer.append((length,operation))
			self._flush()

	def _flush_oldest_operation(self):
		(print_len,print_op)=self._buffer.pop(0)
		assert print_op in "MLR", operation
		if print_op=="M":
			assert self._last_was_matching == False
			self._last_was_matching = True

			self.chain_out_fo.write(str(print_len))
		else:
			assert self._last_was_matching == True
			self._last_was_matching = False
			if print_op=="L":
				self.chain_out_fo.write("\t{}\t{}{}".format(print_len,0,os.linesep))
			elif print_op=="R":
				self.chain_out_fo.write("\t{}\t{}{}".format(0,print_len,os.linesep))

	def _flush(self,final=False):
		while len(self._buffer)>1:
			self._flush_oldest_operation()
		if final:
			if self_buffer[0][1]=="M":
				self._flush_oldest_operation()
			else:
				self._flush_oldest_operation()
				self.chain_out_fo.write("\t{}{}".format(0,os.linesep))

	def process(self):

		while self.chain1.done == False or self.chain2.done == False:

			(c,d)=(self.chain1.count,self.chain2.count)
			(o,p)=(self.chain1.operation,self.chain2.operation)
			m=min(c,d)
			assert m!=0

			print(c,o," - ",d,p)

			# 0-0:0-0, 0-1,1-0
			if   (o,p) in [("B","B"),("L","R")]:
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 1-1:1-1, 1-0:0-1
			elif  (o,p)in [("M","M"),("R","L")]:
				self.add_operation(m,"M")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 1-0:0-0, 1-1:1-0
			elif (o,p) in [("R","B"),("M","R")]:
				self.add_operation(m,"R")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 0-0:0-1, 0-1:1-1
			elif (o,p) in [("B","L"),("L","M")]:
				self.add_operation(m,"L")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 0-1:0-1, 0-1:0-0, 1-1:0-1, 1-1:0-0
			elif (o,p) in [("L","L"),("L","B"),("M","L"),("M","B")]:
				self.chain1.prepend_B(m)

			# 1-0:1-0, 0-0:1-0, 1-0:1-1, 0-0:1-1
			elif (o,p) in [("R","R"),("B","R"),("R","M"),("B","M")]:
				self.chain2.prepend_B(m)

			else:
				assert 1==2

		self._flush(final=True)
