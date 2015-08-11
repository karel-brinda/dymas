class Chain:

	def __init__(self,chain_fn):
		self._chain_fn=chain_fn
		self._chain_fo=open(chain_fn)
		first_line=self._chain_fo.readline().strip()

		[self.score,
		self.tName,
		self.tSize,
		self.tStrand,
		self.tStart,
		self.tEnd,
		self.qName,
		self.qSize,
		self.qStrand,
		self.qStart,
		self.qEnd,
		self.id]=first_line.split("\t")

		self._buffer_blocks=[]

		self._done=False


	def __del__(self):
		self._chain_fo.close()


	def _load_next_line(self):
		line=self._chain_fo.readline().strip()
		parts=line.split("\t")
		assert len(parts) in [1,3]
		if len(parts)==1:
			self._buffer_blocks.append([int(parts[0]),0,0])
			self._done=True
		else:
			self._buffer_blocks.append(map(int,parts))


	def _check_buffer(self):
		if len(self._buffer_blocks)==0 and self._done==False:
			self._load_next_line()

		if len(self._buffer_blocks)>0:
			while sum(self._buffer_blocks[0])=0:
				del self._buffer_blocks[0]



	def insert_gap(self,length):
		if len(self._buffer_blocks)==0 or self._buffer_blocks[0][0]==0:
			self._buffer_blocks.insert(0,[0,length,length])
		else:
			self._buffer_blocks[0][1]+=length
			self._buffer_blocks[0][2]+=length

		self._check_buffer()


	def skip_gap(self,length):
		assert self._buffer_blocks[0][0]==0, self._buffer_blocks[0]
		assert self._buffer_blocks[0][1]>=length, self._buffer_blocks[0]
		assert self._buffer_blocks[0][2]>=length, self._buffer_blocks[0]

		self._buffer_blocks[0][1]-=length
		self._buffer_blocks[0][2]-=length

		self._check_buffer()


	def skip_semigap(self,length):
		assert self._buffer_blocks[0][0]==0,self._buffer_blocks[0] 
		assert self._buffer_blocks[0][1]==0 or self._buffer_blocks[0][2]==0),self._buffer_blocks[0] 

		if self._buffer_blocks[0][1]==0:
			assert self._buffer_blocks[0][2]>=length, self._buffer_blocks[0] 
			self._buffer_blocks[0][2]-=length
		else:
			assert self._buffer_blocks[0][1]>=length, self._buffer_blocks[0] 
			self._buffer_blocks[0][1]-=length

		self._check_buffer()


	def skip_matching(self,length):
		assert self._buffer_blocks[0][1]>=length, self._buffer_blocks[0]
		self._buffer_blocks[0][1]-=length

		self._check_buffer()


	@property
	def length(self):
		self._check_buffer()
		return self._buffer_blocks[0][0]


	@property
	def l_gap(self):
		self._check_buffer()
		return self._buffer_blocks[0][1]


	@property
	def r_gap(self):
		self._check_buffer()
		return self._buffer_blocks[0][2]


	@property
	def done(self):
	    return self._done and len(self._buffer_blocks)==0


	@staticmethod
	def invert_chain(chain1_fn, chain2_fn):
		with open(chain1_fn) as r:
			with open(chain2_fn, "w+") as w:
				first_line=r.readline.strip()
				[
					score,
					tName,
					tSize,
					tStrand,
					tStart,
					tEnd,
					qName,
					qSize,
					qStrand,
					qStart,
					qEnd,
				]=first_line.split()

				w.write("\t".join(
					[
						score,
						qName,
						qSize,
						qStrand,
						qStart,
						qEnd,
						tName,
						tSize,
						tStrand,
						tStart,
						tEnd,
					]
				)+os.linesep)

				for l in r:
					parts=l.strip().split("\t")
					if len(parts)==1:
						w.write(parts[0])
						w.write(os.linesep)
						return
					else:
						assert len(parts)==3
						(size,dt,dq)=parts
						w.write("".join([size,"\t",dq,"\t",dt,os.linesep]))
