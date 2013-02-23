#script for detecting functions defined but not used in scilab

import re
file_name = 'C:\Users\kushal\Documents\python programs\scilab.txt'
file_obj = open(file_name, 'r')
file_data = file_obj.read()
file_obj.close()

def useless(file_data):
    ret = []
    functionline = 'function [^(]*' # detects function declaration line
    results = re.findall(functionline, file_data)
    for result in results:
        name = re.findall("=[^(]*", result)[0][1:].strip()
        count = file_data.count(name)
        if count==1:
            ret.append(name)
    return ret

def var(file_data):
    ret=[]
    temp_names=[]
    var_declaration = '[a-zA-Z_][a-zA-Z0-9_]* *='
    results = re.findall(var_declaration, file_data)
    for result in results:
        name = result.replace("=","").strip()
        count = file_data.count(name)
        if count==1:
           temp_names.append(name)
    line_no=1
    for line in file_data.split("\n"):
        for name in temp_names:
            if name in line:
                ret.append({'var_name':name,'line_no':line_no})
        line_no+=1
    return ret

print 'Unused variables :',var(file_data)
print '\nUnused functions :',useless(file_data)





