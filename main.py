from sodapy import Socrata
from requests import get
import sys
import json
import requests
import os
import pandas as pd
import numpy as np

domain = "data.cityofnewyork.us"
app_token = 'RXeJhe7A7KO2CTm4SURGWOu5y'
identifier = "nc67-uf89"

if __name__ == "__main__":

	client = Socrata(domain, app_token)
	page_size = sys.argv[1]
	num_rows = 49063985
	num_pages = sys.argv[2]

	if len(sys.argv[2]) > 0:
		results = client.get("nc67-uf89", limit = int(num_pages)*int(page_size))
	else: 
		results = client.get("nc67-uf89", limit = num_rows)

	df = pd.DataFrame.from_dict(results)
	df.to_json ('results.json')
	

