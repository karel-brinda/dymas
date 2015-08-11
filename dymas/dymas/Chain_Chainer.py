from .Chain import Chain

class Chain_Chainer:

	def __init__(self,chain1_fn, chain2_fn,new_chain_nf):
		self.chain_out_fo=open(new_chain_nf,"w+")
		self.chain1=Chain(chain1_fn)
		self.chain2=Chain(chain2_fn)
		self.buffer=[]

	def __del__(self):
		self._flush()
		self.chain_out_fo.close()

	def _pseudoflush(self):
		pass

	def _write_line(self,len,l,r):
		pass

	def add_matching(self,length):
		pass

	def add_lgap(self,length):
		pass

	def add_rgap(self,length):
		pass

	def process(self):

		while self.chain1.done == False:
			assert self.chain1.done==self.chain2.done

			(o,p)=(self.chain1.operation,self.chain2.operation)
			(c,d)=(self.chain1.count,self.chain2.count)
			m=min(c,d)
			assert m!=0

			# 0-0:0-0, 0-1,1-0
			if   (o,p) in [("B","B"),("L","R")]:
				chain1.skip(m)
				chain2.skip(m)

			# 1-1:1-1, 1-0:0-1
			elif  (o,p)in [("M","M"),("R","L")]:
				self.add_matching(m)
				chain1.skip(m)
				chain2.skip(m)

			# 1-0:0-0, 1-1:1-0
			elif (o,p) in [("R","B"),("M","R")]:
				self.add_rgap(m)
				chain1.skip(m)
				chain2.skip(m)

			# 0-0:0-1, 0-1:1-1
			elif (o,p) in [("B","L"),("L","M")]:
				self.add_lgap(m)
				chain1.skip(m)
				chain2.skip(m)

			# 0-1:0-1, 0-1:0-0, 1-1:0-1, 1-1:0-0
			elif (o,p) in [("L","L"),("L","B"),("M","L"),("M","B")]:
				chain1.add_B(m)

			# 1-0:1-0, 0-0:1-0, 1-0:1-1, 0-0:1-1
			elif (o,p) in [("R","R"),("B","R"),("R","M"),("B","M")]:
				chain2.add_B(m)
				