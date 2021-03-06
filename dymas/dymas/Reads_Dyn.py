from .Reads import Reads
import math

class Reads_Dyn(Reads):

	def __init__(self,
				fastq_1_fn,
				coverage,
				coverage_per_iteration,
				fastq_2_fn=None,
				remapping=True,
			):

		super().__init__(
				fastq_1_fn=fastq_1_fn,
				fastq_2_fn=fastq_2_fn,
				coverage=coverage,
			)

		self.coverage_per_iteration=coverage_per_iteration
		self.iterations=int(math.ceil(coverage/coverage_per_iteration))
		self.reads_per_iteration=int(math.ceil((coverage_per_iteration/coverage)*self.reads))
		self.remapping=remapping

	def create_fastq_iteration(self,fastq_fn,iteration):
		with open(self.fastq_1_fn) as inp:
			with open(fastq_fn,"w+") as outp:

				if self.remapping:
					first_line=0
				else:
					first_line=self.reads_per_iteration*iteration*4

				last_line=self.reads_per_iteration*(iteration+1)*4
				print("Reads - interval: {} - {}".format(first_line,last_line))

				for i,line in enumerate(inp):

					if i >= first_line and i<last_line:
						if line is None or line.strip()=="":
							continue
							#print(line)
						if i%4==0:
							read_nb=i//4
							orig_iteration=read_nb//self.reads_per_iteration
							outp.write("@dyn{}".format(str(orig_iteration).zfill(3)))
							outp.write(line[1:])
						else:
							outp.write(line)

