import os,pyautogui,datetime
tm = datetime.datetime.now()
pic_name = datetime.datetime.strftime(tm,"%d%Y%H%M%S%f")[:-3]
pic_name= int(pic_name)//100
pic_name = str(pic_name)
pic = pyautogui.screenshot("/home/nazrul/Documents/screenshots/myshot"+pic_name+".png")
