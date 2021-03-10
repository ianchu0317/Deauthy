import os
from time import sleep
from colorama import init, Fore, Style


def activate(interface, channel):
	print(Fore.YELLOW + "\n\n ***SETTING INETERFACE*** \n")
	print(Fore.GREEN + f"Stopping {interface}")
	os.system(f"ifconfig {interface} down")
	sleep(1)

	print(Fore.GREEN + "Setting monitor mode")
	os.system(f"iwconfig {interface} mode monitor")
	sleep(1)

	print(Fore.GREEN + "Setting channel")
	os.system(f"iwconfig {interface} channel {channel}")
	sleep(1)

	print(Fore.GREEN + f"Starting {interface}")
	os.system(f"ifconfig {interface} up")
	sleep(1)
	print(Fore.YELLOW + "DONE !")


def desactivate(interface):
	print(Fore.YELLOW + "\n\n***SETTING INTERFACE***\n")
	print(Fore.GREEN + f"Stopping {interface}")
	os.system(f"ifconfig {interface} down")
	sleep(1)

	print(Fore.GREEN + "Setting Managed Mode")
	os.system(f"iwconfig {interface} mode managed")
	sleep(1)

	print(Fore.GREEN + f"Setting '{interface}' up")
	os.system(f"ifconfig {interface} up")
	sleep(1)



	print(Fore.YELLOW + "DONE !")
