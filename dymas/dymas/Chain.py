class Chain:

	def __init__(self,chain_fn):
		self._chain_fn=chain_fn
		self._chain_fo=open(chain_fn)

		self.last_line=self._chain_fo.readline().strip()

		parts=self.last_line.split(" ")
		print(parts)
		[
			_,
			self.score,
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
			self.id,
		]=parts

		self.score = int(self.score)
		#self.tName = int(self.tName)
		self.tSize = int(self.tSize)
		#self.tStrand = int(self.tStrand)
		self.tStart = int(self.tStart)
		self.tEnd = int(self.tEnd)
		#self.qName = int(self.qName)
		self.qSize = int(self.qSize)
		#self.qStrand = int(self.qStrand)
		self.qStart = int(self.qStart)
		self.qEnd = int(self.qEnd)
		self.id = int(self.id)

		assert self.tName==self.qName

		assert self.tStrand=="+"
		assert self.qStrand=="+"

		assert self.tStart==0
		assert self.qStart==0

		assert self.qEnd==self.qSize
		assert self.tEnd==self.tSize

		self._buffer=[]

		self._done=False
		self._counter_matches=0
		self._counter_both_insertions=0
		self._counter_left_insertions=0
		self._counter_right_insertions=0


	def __del__(self):
		self._chain_fo.close()

	# M = 1-1
	# L = 0-1
	# R = 1-0
	# B = 0-0
	def _load_next_line(self):
		self.last_line=self._chain_fo.readline().strip()
		print("loading line {}:{}".format(self._chain_fn,self.last_line))
		if len(self.last_line)>0:
			parts=self.last_line.split()
			assert len(parts) in [1,3]
			if len(parts)==1:
				M=int(parts[0])
				self._append_operation_to_buffer(M,"M")
				self._done=True
			else:
				M=int(parts[0])
				L=int(parts[2])
				R=int(parts[1])
				self._append_operation_to_buffer(M,"M")
				self._append_operation_to_buffer(min(L,R),"B")
				self._append_operation_to_buffer(L-min(L,R),"L",)
				self._append_operation_to_buffer(R-min(L,R),"R")


	def _append_operation_to_buffer(self, length, operation):
		assert operation in ["M","B","L","R"]
		if length>0:
			self._buffer.append([length,operation])


	def _update_buffer(self):
		while len(self._buffer)>0 and self._buffer[0][0]==0:
			del self._buffer[0]

		if len(self._buffer)==0 and self._done==False:
			self._load_next_line()


	def prepend_B(self,length):
		assert length>0
		self._buffer.insert(0,[length,"B"])

	def skip(self,length,update_counters=True):
		#print("skiping",length)
		assert len(self._buffer)>0
		assert self._buffer[0][0]>=length

		op=self._buffer[0][1]

		self._buffer[0][0]-=length
		self._update_buffer()

		if update_counters:
			assert op in "MLRB", op
			if op=="M":
				self._counter_matches+=length
			elif op == "L":
				self._counter_left_insertions+=length
			elif op == "R":
				self._counter_right_insertions+=length
			elif op == "B":
				self._counter_both_insertions+=length


	@property
	def buffer(self):
		return self._buffer


	@property
	def count(self):
		if len(self._buffer)==0:
			self._load_next_line()			
		assert len(self._buffer)>0
		#print(self._buffer)
		return self._buffer[0][0]

	@property
	def operation(self):
		if len(self._buffer)==0:
			self._load_next_line()			
		assert len(self._buffer)>0
		return self._buffer[0][1]

	@property
	def done(self):
		return self._done and len(self._buffer)==0

	@property
	def counter_left_insertions(self):
		return self._counter_left_insertions

	@property
	def counter_right_insertions(self):
		return self._counter_right_insertions
	
	@property
	def counter_both_insertions(self):
		return self._counter_both_insertions
	
	@property
	def counter_matches(self):
		return self._counter_matches
	
	@property
	def counters_sum(self):
		return sum(
			[
				self.counter_left_insertions,
				self.counter_right_insertions,
				self.counter_both_insertions,
				self.counter_matches,
			])
	
	@property
	def remains_left(self):
		return self.tSize-self.counter_matches-self.counter_right_insertions
	
	@property
	def remains_right(self):
		return self.qSize-self.counter_matches-self.counter_left_insertions
	
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
