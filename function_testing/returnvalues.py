def returnvalues(file_data): # file_data is without comments
	
	args_with_no_return = []
	
	func_declaration_line = re.findall("function [^=]*",file_data)
	for func_declaration_statement in func_declaration_line:
		outputargs = func_declaration_statement.replace("function",'').strip('[ ]')
		outputarg = [word.strip() for word in outputargs.split(',') if word.strip()]
	
	for element in outputarg:
		if file_data.count(element) < 2:
			args_with_no_return.append(element)

	return args_with_no_return
