from wifi import Cell


def get_networks(interface):
	networks = Cell.all(f"{interface}")
	return list(networks)
