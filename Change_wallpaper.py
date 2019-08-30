#!/usr/bin/env python3
import subprocess,os,random,pprint
def quote_file_name(name):
	li = name.split(" ")
	return "\\ ".join(li)
def change_wallpaper():
	folder = "/home/nazrul/Pictures/"
	li = os.listdir(folder)
	#pprint.pprint(li)
	rand = random.randint(0,len(li)-1)
	file_name = li[rand]
	#print(file_name)
	file_path = os.path.join(folder,file_name)
	#print(file_path)
	command = "gsettings set org.gnome.desktop.background picture-uri "
	commandArgs = command.split()
	commandArgs.append(file_path)
	#pprint.pprint(commandArgs)
	subprocess.call(commandArgs)
	#f_command = command+file_path
	#print(f_command)
	#os.system(f_command)
change_wallpaper()	
