from sodapy import Socrata
from requests import get
import sys
import json

if __name__ == "__main__":
	client = Socrata("data.cityofnewyork.us", 'RXeJhe7A7KO2CTm4SURGWOu5y')
	page_size = sys.argv[1]
	results = client.get("nc67-uf89", limit=page_size)
	print(results)

