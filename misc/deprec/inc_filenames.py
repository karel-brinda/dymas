def fq_file():
	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		"reads",
		"{}__{}_{}_{}.fq".format(
			config["G_reference"],
			config["R_read_length"],
			config["R_rate_of_mutations"],
			config["R_error_rate"] ) 
		)

def config_file():
	return os.path.join(
		"experiments",
		".{}.conf".format(config["G_experiment_name"])
	)
	
def report_file():
	return os.path.join(
		"experiments",
		"report__{}__{}".format(
				config["G_experiment_name"],
				config["G_mapper"]
			)
		)

def bam_file(method,it):
	if DEBUG:
		print("Required bam_file",method,it)

	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"bam",
		"{}.{}.{}_{}.bam".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
	))

def fa_file(method,it):
	if DEBUG:
		print("Required fa_file",method,it)

	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"fa",
		"{}.{}.{}_{}.fa".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
		))


def vcf_file(method,it):
	if DEBUG:
		print("Required vcf_file",method,it)
	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"vcf",
		"{}.{}.{}_{}.vcf".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
		))

def vcf_c_file(method,it):
	if DEBUG:
		print("Required vcf_c_file",method,it)

	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"vcf",
		"{}.{}.{}_{}.vcf.gz".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
		))

def vcf_c_i_file(method,it):
	if DEBUG:
		print("Required vcf_c_i_file",method,it)

	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"vcf",
		"{}.{}.{}_{}.vcf.gz.tbi".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
		))

def chain_file(method,it):
	if DEBUG:
		print("Required chain_file",method,it)

	return os.path.join(
		"experiments",
		config["G_experiment_name"],
		config["G_mapper"],
		method,
		"chain",
		"{}.{}.{}_{}.chain".format(
			config["G_experiment_name"],
			config["G_mapper"],
			method,
			format_nb(it)
		))
