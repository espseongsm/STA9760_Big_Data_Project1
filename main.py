from sodapy import Socrata
from requests import get
import sys
import json
import requests
import os
import pandas as pd
import numpy as np

if __name__ == "__main__":
	client = Socrata("data.cityofnewyork.us", 'RXeJhe7A7KO2CTm4SURGWOu5y')
	page_size = sys.argv[1]
	results = client.get("nc67-uf89", limit=page_size, offset=page_size)
	df = pd.DataFrame.from_dict(results)
	df.to_json ('results.json')
	

