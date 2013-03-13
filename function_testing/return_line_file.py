def return_line_no(keyword_list,file_list):
	file_keyword_list = []
	for file_name in file_list:
		import os
		path = (os.getcwd())

		#
		file_obj = open(path+'/'+file_name,'r')
		file_text = file_obj.read()
		file_obj.close()
		#file_text = rm_comments(file_text) # file_text should be commentless
		
		# Iterate for keywords
		for keyword in keyword_list:
		
			if file_text.count(keyword) != 0:
				file_text_list = file_text.splitlines()
				line_no = 0
				for line in file_text_list:
					line_no += 1
					if line.count(keyword) != 0:
						file_keyword_list.append([line_no, file_name])
			else:
				pass
			
		#except:
		#print("File " + file_name + " not found")
		
	return file_keyword_list
		


#p  = open('sample.sci')
lis=['sample.sci','sample_header.sci','abc.sce']
keywords = ['image_mat_size','sum_vector','header_var']

print "ECH"
print return_line_no(keywords,lis)
 
