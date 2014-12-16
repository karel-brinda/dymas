def format_nb(x):
	return str(x).zfill(4) if isinstance(x,int) else x
	

def message(x):
	return """
==========================================================================================
{x}

	input:	{{input}}

	output:	{{output}}
==========================================================================================
	
	""".format(x=x)
		
	
