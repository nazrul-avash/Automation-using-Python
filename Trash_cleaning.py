import os,shutil
def clean_trash():
	root_dir = "/home/nazrul/.local/share/Trash/files/"
	for f in os.listdir(root_dir):
		file_path = os.path.join(root_dir,f)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
				print(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
				print(file_path)
		except Exception as e:
			print(e)			
clean_trash()		