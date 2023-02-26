import os
from colorama import Fore, Style, init
from time import sleep
import shutil

init()
os.system('cls')

print(Fore.GREEN + "┌───(" + Fore.BLUE + "kali@kali" + Fore.GREEN + ")-[" + Fore.WHITE + "~/Desktop" + Fore.GREEN + "]")
launch = input(Fore.GREEN + "└─" + Fore.BLUE + "$ " + Fore.GREEN)

def setup():
	print(Fore.WHITE + Style.NORMAL + "\nSetting up files...")

	try:
		print("Creating .minecraft folder")
		sleep(2)
		os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.minecraft')

		print("Creating launcher_accounts.json")
		sleep(2)
		filePath = shutil.copy('.minecraft/launcher_accounts.json', 'C:/Users/BeingUzeless/AppData/Roaming/.minecraft')
	
		print("Creating launcher_accounts.json")
		sleep(2)
		filePath = shutil.copy('.minecraft/launcher_profiles.json', 'C:/Users/BeingUzeless/AppData/Roaming/.minecraft')
	
		print("Creating launcher_settings.json")
		sleep(2)
		filePath = shutil.copy('.minecraft/launcher_settings.json', 'C:/Users/BeingUzeless/AppData/Roaming/.minecraft')
	
		print("Creating launcher_ui_state.json")
		sleep(2)
		filePath = shutil.copy('.minecraft/launcher_ui_state.json', 'C:/Users/BeingUzeless/AppData/Roaming/.minecraft')
	
		print("Creating treatment_tags.json")
		sleep(2)
		filePath = shutil.copy('.minecraft/treatment_tags.json', 'C:/Users/BeingUzeless/AppData/Roaming/.minecraft')
	
		print("Setting up versions")
		sleep(2)
		os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.minecraft/versions')
		print("Done!")
	except:
		print(Fore.RED + Style.BRIGHT + "\n.minecraft folder already exist! Please delete it and restart this script." + Fore.WHITE + Style.NORMAL)

def start():
	print(Fore.WHITE + Style.NORMAL + "\nPreparing")
	sleep(2)
	print("Launching...")
	os.system("Minecraft.exe")

if launch == "help":
	print(Fore.WHITE + Style.NORMAL + "\nThis is the help page, you can find every command this software have:")
	print(Fore.RED + Style.BRIGHT + "               <>" + Fore.WHITE + Style.NORMAL + " are required" + Fore.LIGHTBLACK_EX + " | " + Fore.BLUE + Style.BRIGHT + "[]" + Fore.WHITE + Style.NORMAL + " are optional")
	print(Style.BRIGHT + "\nhelp" + Style.NORMAL + " - It return this help menu")
	print(Style.BRIGHT + "package list" + Style.NORMAL + " - You can see the list of available package you can download")
	print(Style.BRIGHT + "sudo apt install " + Fore.RED + "<package>" + Fore.WHITE + Style.NORMAL + " - You can install the package wanted")
	input(Style.BRIGHT + "start " + Fore.RED + "<package>" + Fore.WHITE + Style.NORMAL + " - You can start any package downloaded\n")
elif launch == "package list":
	print()
elif launch == "sudo apt install Minecraft":
	setup()
elif launch == "start Minecraft":
	start()
else:
	print(Fore.RED + "Commande inconnue ! ")