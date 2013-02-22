#!/usr/bin/python2.7	

# multi-line comment  => done
# multi-line uncomment
# single var  handle exec and loops
# show diff after execution
# handle ; and missing end

import argparse

parser = argparse.ArgumentParser(description="A simple script to save you from mildly terrible scilab scripting")
parser.add_argument("file", help="requires a valid file name")

group = parser.add_mutually_exclusive_group()
group.add_argument("-c","--comment_all", help="multi-line comment given document specified by ##  markers", action="store_true")
group.add_argument("-u", "--uncomment_all", help="multi-line UNcomment if previously commented using yelp", action = "store_true")
parser.add_argument("-f", help="Force the script to write changes directly to the file", action="store_true")

args = parser.parse_args()

# File opening and read it into file_data variable
file_obj = open(args.file, 'r')
file_data = file_obj.read()
file_obj.close()

def comment_all(str_data):
	# Check for number of ##, if the number is odd, then user is on way to destroy code
	if str_data.count("##")%2 != 0:
		print("There are odd number of ## markers in document, please correct it")
		return (-1)
	else:
		list_data = str_data.splitlines()
		
		count = 0
		start_marker = []
		end_marker = []

		# iterating for each sentence
		for i in list_data:
			count+=1
			if i.startswith("##"):
				start_marker.append(count)
			elif i.endswith("##"):
				end_marker.append(count)

		for i in start_marker:
			line_iterator = range((i-1),(end_marker[start_marker.index(i)])) # Use of (i-1) so that it includes the line which contains #

			# Add // to those section
			for j in line_iterator:
				list_data[j] = "//" + list_data[j]			
		
		# Convert list_data to a string modified_content
		modified_content = ""
		for i in list_data:
			modified_content = modified_content + i + "\n"
			
		# If --force option is set, then write in same file
		if args.f:
			# reopen original file
			file_obj = open(args.file, 'w')
			file_obj.write(modified_content)
			file_obj.close()
		else:
			write_other_file = open(args.file+"_modified", 'w')
			write_other_file.write(modified_content)
			write_other_file.close()

# check for  
if args.comment_all:
	print "commenting file"
	comment_all(file_data)
if args.uncomment_all:
	print "uncommenting file"

