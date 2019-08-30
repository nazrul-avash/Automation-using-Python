#!/usr/bin/env python3
#this script used to empty trash/recycle bin automatically. add this to cronjob or to something similar to cronjob as per your operating system
import os,shutil
def clean_trash():
	root_dir = "/home/nazrul/.local/share/Trash/files/" #this is where my trash lives
	for f in os.listdir(root_dir):
		file_path = os.path.join(root_dir,f)
		try:
			if os.path.isfile(file_path): #check if its a file
				os.unlink(file_path)
				print(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
				print(file_path)
		except Exception as e:
			print(e)			
clean_trash()		