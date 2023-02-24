import time
import os
import progressbar
from colorama import init
from colorama import Fore, Style
from time import sleep
import shutil

init()

print(Style.BRIGHT + Fore.BLUE)
bar = progressbar.ProgressBar(maxval=10.0, widgets=[
	' Launching... ',
	progressbar.Bar(left='| ', marker='█', right=' | '),
	progressbar.SimpleProgress(),
]).start()

t = 0.0
while t <= 10.0:
	bar.update(t)
	time.sleep(0.02)
	t += 0.1
bar.finish()
os.system('cls')

print(Fore.GREEN + "┌───(" + Fore.BLUE + "kali@kali" + Fore.GREEN + ")-[" + Fore.WHITE + "~/Desktop" + Fore.GREEN + "]")
launch = input(Fore.GREEN + "└─" + Fore.BLUE + "$ " + Fore.GREEN)

if launch == "sudo apt-get install Minecraft":
	print(Fore.WHITE + "Setting up files...")
	os.mkdir('C:/Users/patri/AppData/Roaming/.test')
	filePath = shutil.copy('file.txt', 'C:/Users/patri/AppData/Roaming/.test')
	print("Done!")