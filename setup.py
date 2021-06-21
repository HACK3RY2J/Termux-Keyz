import os
import sys


def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


clr()
os.system('figlet -f slant Termux Keyz | lolcat -as 50')
az = input('Version 1.0(Basic)\nUpdate Before 31 August 2021\n\n\nWelcome To Termux Key Modification.\n\n1.Enable Extra Keys\n2.Disable Extra Keys\n3.Exit\n>>>')
if az == "1":
	os.system("mkdir $HOME/.termux/ ;echo \"extra-keys = [['ESC','/','-','HOME','UP','END'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT']]\" >> $HOME/.termux/termux.properties && termux-reload-settings")
	clr()
	print("Succesfully Enabled Extra Keys\nRestart Termux To Auto-Adjust Keys")
elif az == "2":
	os.system("mkdir $HOME/.termux/ ;echo \"extra-keys = [['ESC','TAB','CTRL','ALT','-','DOWN','UP']]\" >> $HOME/.termux/termux.properties && termux-reload-settings")
	clr()
	print("Succesfully Disabled Extra Keys\nRestart Termux To Auto-Adjust Keys")
elif az == "3":
	exit()
else:
	print('Wrong Input Detected')
	os.system('python setup.py')
