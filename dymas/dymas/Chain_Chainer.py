import os

from .Chain import Chain

class Chain_Chainer:

	def __init__(self,chain1_fn, chain2_fn,new_chain_fn):
		self.chain_out_fo=open(new_chain_fn,"w+")
		self.chain1=Chain(chain1_fn)
		self.chain2=Chain(chain2_fn)
		self._buffer=[]


		self._last_was_matching=False

		try:
			while(self.process_next_sequence()):
				pass
		except:
			self.debug_status()
			raise

	def debug_status(self):
			print()
			print("/------------")
			print("| CHAIN CHAINER STATUS")
			print("| chain 1: '{}'".format(self.chain1.chain_fn))
			print("|          buffer: '{}'...".format(
					" ".join(map(lambda x:"{}{}".format(x[0],x[1]),self.chain1.buffer[:10]))
				))
			print("|          counters:  M={:<8}  B={:<8}  L={:<8}  R={:<8}  (sum={})".format(
					self.chain1.counter_matches,
					self.chain1.counter_both_insertions,
					self.chain1.counter_left_insertions,
					self.chain1.counter_right_insertions,
					self.chain2.counters_sum,
				))
			print("|          remains:   l={:<8}  r={:<8}".format(
					self.chain1.remains_left,
					self.chain1.remains_right,
				))
			print("| chain 2: '{}'".format(self.chain2.chain_fn))
			print("|          buffer: '{}'...".format(
					" ".join(map(lambda x:"{}{}".format(x[0],x[1]),self.chain2.buffer[:10]))
				))
			print("|          counters:  M={:<8}  B={:<8}  L={:<8}  R={:<8}  (sum={})".format(
					self.chain2.counter_matches,
					self.chain2.counter_both_insertions,
					self.chain2.counter_left_insertions,
					self.chain2.counter_right_insertions,
					self.chain2.counters_sum,
				))
			print("|          remains:   l={:<8}  r={:<8}".format(
					self.chain2.remains_left,
					self.chain2.remains_right,
				))
			print("\------------")
			print()

	def __del__(self):
		self.chain_out_fo.close()

	def add_operation(self,length,operation):
		assert length>=0
		if length>0:
			if len(self._buffer)==0:
				self._buffer.append([length,operation])
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
						self._buffer.append([length,operation])
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
			if print_op=="R":
				self.chain_out_fo.write("\t{}\t{}{}".format(print_len,0,os.linesep))
			elif print_op=="L":
				self.chain_out_fo.write("\t{}\t{}{}".format(0,print_len,os.linesep))

	def _flush(self,final=False):
		while len(self._buffer)>1:
			self._flush_oldest_operation()
		if final:
			if len(self._buffer)==1 and self._buffer[0][1]=="M":
				self.chain_out_fo.write("{}{}".format(self._buffer[0][0],os.linesep))
			else:
				self._flush_oldest_operation()
				self.chain_out_fo.write("{}{}".format(0,os.linesep))

	def process_next_sequence(self):

		a=self.chain1.load_next_sequence()
		b=self.chain2.load_next_sequence()
		assert a==b

		if a is None:
			return False

		assert self.chain1.qSize==self.chain2.tSize
		assert self.chain1.tName==self.chain1.qName==self.chain2.tName==self.chain2.qName
		assert self.chain1.qStart==self.chain2.tStart
		assert self.chain1.qEnd==self.chain2.tEnd
		assert self.chain1.qSize==self.chain2.tSize

		self.chain_out_fo.write(" ".join(
			map(str,[
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
			]))+os.linesep
		)

		while self.chain1.buffer!=[] and self.chain2.buffer!=[]:

			(c,d)=(self.chain1.count,self.chain2.count)
			(o,p)=(self.chain1.operation,self.chain2.operation)
			m=min(c,d)
			assert m!=0

			print("Processing: {}{}-{}{}".format(c,o,d,p))

			# 0-1,1-0
			if (o,p) in [("L","R")]:
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 1-1:1-1, 1-0:0-1
			elif  (o,p)in [("M","M"),("R","L")]:
				self.add_operation(m,"M")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 1-0:0-0, 1-1:1-0
			elif (o,p) in [("M","R")]:
				self.add_operation(m,"R")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 0-0:0-1, 0-1:1-1
			elif (o,p) in [("L","M")]:
				self.add_operation(m,"L")
				self.chain1.skip(m)
				self.chain2.skip(m)

			# 0-1:0-1, 0-1:0-0, 1-1:0-1, 1-1:0-0
			elif (o,p) in [("L","L"),("M","L")]:
				self.chain2.skip(m)
				self.add_operation(m,"L")

			# 1-0:1-0, 0-0:1-0, 1-0:1-1, 0-0:1-1
			elif (o,p) in [("R","R"),("R","M"),]:
				self.add_operation(m,"R")
				self.chain1.skip(m)

			else:
				assert 1==2

			self.debug_status()
			assert self.chain1.counters_sum==self.chain2.counters_sum
			assert self.chain1.remains_right==self.chain2.remains_left


		self._flush(final=True)
		self.chain_out_fo.write(os.linesep)
		return True
