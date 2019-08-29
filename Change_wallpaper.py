import subprocess,os,random,pprint
def change_wallpaper():
	folder = "/home/nazrul/Pictures/"
	li = os.listdir(folder)
	pprint.pprint(li)
	rand = random.randint(0,len(li)-1)
	print(rand)
	file_path = os.path.join(folder,li[rand])
	print(file_path)
	command = "gsettings set org.gnome.desktop.background picture-uri " + file_path
	commandArgs = command.split()
	subprocess.call(commandArgs)
