def format_nb(x):
	return str(x).zfill(4) if isinstance(x,int) else x
	
def fq_file():
	return os.path.join(
		config["G_experiment_name"],
		"reads",
		"{}__{}_{}_{}.fq".format(
			config["G_reference"],
			config["R_read_length"],
			config["R_rate_of_mutations"],
			config["R_error_rate"] ) 
		)

def config_file():
	return ".{}.conf".format(
			config["G_experiment_name"],
		)
	
def report_file():
	return "report__{}__{}".format(
		config["G_experiment_name"],
		config["G_mapper"]
	)

def s_prefix():
	return os.path.join(
		config["G_experiment_name"],
		config["G_mapper"],
		"static"
	)

def s_bam(it):
	return os.path.join(
		s_prefix(),
		"bam",
		"{}.{}.s_{}.bam".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
	))

def s_fa(it):
	return os.path.join(
		s_prefix(),
		"fa",
		"{}.{}.s_{}.fa".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
		))

def s_vcf(it):
	return os.path.join(
		s_prefix(),
		"vcf",
		"{}.{}.s_{}.vcf".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
		))


def d_prefix():
	return os.path.join(
		config["G_experiment_name"],
		config["G_mapper"],
		"dynamic")

def d_bam(it):
	return os.path.join(
		d_prefix(),
		"bam",
		"{}.{}.d_{}.bam".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
		))

def d_fa(it):
	return os.path.join(
		d_prefix(),
		"fa",
		"{}.{}.d_{}.fa".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
		))

def d_vcf(it):
	return os.path.join(
		d_prefix(),
		"vcf",
		"{}.{}.d_{}.vcf".format(
			config["G_experiment_name"],
			config["G_mapper"],
			format_nb(it)
		))


def message(x):
	return """
	==========================================================================================
	{x}
		input:	{{input}}
		output:	{{output}}
	==========================================================================================
	
	""".format(x=x)
		
	
