import time

def format_nb(x):
	return str(x).zfill(4) if isinstance(x,int) else x
	

def message(x,):
	return """
==========================================================================================
{x}
	time:   {time}
	input:	{{input}}
	output:	{{output}}
==========================================================================================
	
	""".format(x=x,time=time.strftime("%a, %d %b %Y %H:%M:%S"))
		
	
