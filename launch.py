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
	os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.test')
	filePath = shutil.copy('.minecraft/launcher_accounts.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test')
	filePath = shutil.copy('.minecraft/launcher_profiles.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test')
	filePath = shutil.copy('.minecraft/launcher_settings.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test')
	filePath = shutil.copy('.minecraft/launcher_ui_state.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test')
	filePath = shutil.copy('.minecraft/treatment_tags.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test')

	os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.test/versions')
	os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.test/versions/1.19.3')
	filePath = shutil.copy('.minecraft/versions/1.19.3/1.19.3.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test/versions/1.19.3')
	os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.test/versions/1.19.4-pre1')
	filePath = shutil.copy('.minecraft/versions/1.19.3/1.19.4-pre1.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test/versions/1.19.4-pre1')
	filePath = shutil.copy('.minecraft/versions/version_manifest_v2.json', 'C:/Users/BeingUzeless/AppData/Roaming/.test/versions')
	
	os.mkdir('C:/Users/BeingUzeless/AppData/Roaming/.test/webcache2')
	print("Done!")