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

	def add_matches(l):
		pass

	def add_lgap(gap):
		pass

	def add_rgap(gap):
		pass

	def process(self):

		while self.chain1.done == False:
			assert self.chain1.done==self.chain2.done

			minimum=min(self.chain1.l_gap, self.chain1.r_gap, self.chain2.l_gap, self.chain2.r_gap, )
			maximum=max(self.chain1.l_gap, self.chain1.r_gap, self.chain2.l_gap, self.chain2.r_gap, )
			assert minimum>=0
			
			if minimum!=0:
				# gaps everywhere
				# 0-0  0-0
				
				chain1.skip_gap(minimum)
				chain2.skip_gap(minimum)
				continue

			if maximum==0:
				# no gaps
				# 1-1  1-1
				
				length=min(self.chain1.length,self.chain2.length)
				self.add_matches(length)
				self.chain1.skip_matching(length)
				self.chain2.skip_matching(length)
				continue


			if self.chain1.r_gap>0 and self.chain2.l_gap>0:
				# internal gap overlap => report
				# ?-0  0-?
				
				if self.chain1.l_gap>0 and self.chain2.r_gap==0:
					# 0-0  0-1
					
					length=min(self.chain1.l_gap,self.chain1.r_gap,self.chain2.l_gap)
					self.add_lgap(length)
					self.chain1.skip_gap(length)
					self.chain2.skip_semigap(length)
					continue

				if self.chain1.l_gap==0 and self.chain2.r_gap>0:
					# 1-0  0-0
					
					length=min(self.chain1.r_gap,self.chain2.l_gap,self.chain2.r_gap)
					self.add_rgap(length)
					self.chain1.skip_semigap(length)
					self.chain2.skip_gap(length)
					continue

				if self.chain1.l_gap==0 and self.chain2.r_gap==0:
					# 1-0  0-1

					length=min(self.chain1.r_gap,self.chain2.l_gap)
					self.add_matches(length)
					chain1.skip_semigap(length)
					chain2.skip_semigap(length)
					continue


				assert 1==2

			if self.chain1.r_gap>0 or self.chain2.l_gap>0:
				# no internal overlap but some gap exists

				if self.chain1.r_gap>0:
					# ?-0  1-?
					self.chain2.insert_gap(self.chain1.r_gap)
					continue

				if self.chain2.l_gap>0:
					# ?-1  0-?
					self.chain1.insert_gap(self.chain2.l_gap)
					continue

				assert 1==2


			if self.chain1.r_gap==0 and self.chain2.l_gap==0:
				# zero gaps in overlap
				# ?-1  1-?

				if self.chain1.l_gap>0 and self.chain2.r_gap==0:
					# 0-1  1-1
					length=min(self.chain1.l_gap)
					self.add_lgap(length)
					self.chain1.skip_semigap(length)
					self.chain2.skip_matching(length)



			assert 1==2








	



