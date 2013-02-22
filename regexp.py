#script for detecting functions defined but not used in scilab

import re
file_obj = open('C:\Users\kushal\Documents\python programs\scilab.txt', 'r')
file_data = file_obj.read()
file_obj.close()

def useless(file_data):
    ret = []
    functionline = 'function +[^{]*[\n\t ]*{' # detects function declaration line
    results = re.findall(functionline, file_data)
    for result in results:
        name = re.findall("= *[^(]*", result)[0][1:].strip() 
        if file_data.count(name)==1:
            ret.append(name)
            print name
    return ret

useless(file_data)




