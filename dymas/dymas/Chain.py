class Chain:

	def __init__(self,chain_fn):
		self._chain_fn=chain_fn
		self._chain_fo=open(chain_fn)
		first_line=self._chain_fo.readline().strip()

		parts=first_line.split(" ")
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

		self._buffer=[]

		self._done=False


	def __del__(self):
		self._chain_fo.close()

	# M = 1-1
	# L = 0-1
	# R = 1-0
	# B = 0-0
	def _load_next_line(self):
		line=self._chain_fo.readline().strip()
		print("line {}:{}".format(self._chain_fn,line))
		if len(line)>0:
			parts=line.split()
			print(parts)
			assert len(parts) in [1,3]
			if len(parts)==1:
				M=int(parts[0])
				self._append_operation_to_buffer(M,"M")
				self._done=True
			else:
				M=int(parts[0])
				L=int(parts[1])
				R=int(parts[2])
				self._append_operation_to_buffer(M,"M")
				self._append_operation_to_buffer(min(L,R),"B")
				self._append_operation_to_buffer(L-min(L,R),"L",)
				self._append_operation_to_buffer(R-min(L,R),"R")


	def _append_operation_to_buffer(self, length, operation):
		assert operation in ["M","B","L","R"]
		if length>0:
			self._buffer.append([length,operation])


	def _prepend_operation_to_buffer(self, length, operation):
		assert operation in ["M","B","L","R"]
		if length>0:
			self._buffer.insert(0,[length,operation])


	def _update_buffer(self):
		while len(self._buffer)>0 and self._buffer[0][0]==0:
			del self._buffer[0]

		if len(self._buffer)==0 and self._done==False:
			self._load_next_line()


	def prepend_B(self,length):
		if length>0:
			self._prepend_operation_to_buffer(length,"B")
			self._update_buffer()


	def skip(self,length):
		print("skiping",length)
		assert len(self._buffer)>0
		assert self._buffer[0][0]>=length

		self._buffer[0][0]-=length
		self._update_buffer()


	@property
	def count(self):
		if len(self._buffer)==0:
			self._load_next_line()			
		assert len(self._buffer)>0
		print(self._buffer)
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
