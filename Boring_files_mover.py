#!/usr/bin/env python3
import os,shutil
src = "/home/nazrul/Pictures/"
dest = "/home/nazrul/Downloads/Screenshots/"
genOb = os.walk(src) 
file_num= 1
for d in genOb:
	for f in d[2]:
		if "Screenshot" in f:
			print(f)
			shutil.copy(d[0]+"/"+f,dest) #
			os.unlink(d[0]+"/"+f)
			conztinue
		temp = os.path.splitext(f)
		print(d[0]+"wall"+str(file_num)+temp[1]+" <<<<<<  "+d[0]+f)	
		os.rename(d[0]+f,d[0]+"wall"+str(file_num)+temp[1])
		file_num += 1	
