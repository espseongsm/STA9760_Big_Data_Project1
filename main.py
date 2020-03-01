from sodapy import Socrata

if __name__ == "__main__":
	client = Socrata("data.cityofnewyork.us", 'RXeJhe7A7KO2CTm4SURGWOu5y')

	result = client.get("nc67-uf89", limit=page_size*num_pages)
	print(result.json())
