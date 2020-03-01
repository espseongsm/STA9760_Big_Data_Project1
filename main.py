from sodapy import Socrata
from requests import get
import sys
import argparse
import json
import requests
import os
import pandas as pd
import numpy as np

domain = "data.cityofnewyork.us"
app_token = os.environ['APP_KEY']
identifier = "nc67-uf89"

#if __name__ == "__main__":

client = Socrata(domain, app_token)
num_rows = 49063985

#def main():
parser = argparse.ArgumentParser(usage="main.py --page_size=page_size --num_pages=num_pages --output=output_filename", description="put the parameters")
	
parser.add_argument('--page_size', type=int, help="put the page size")
parser.add_argument('--num_pages', type=int, help="put the number of pages")
parser.add_argument('--output', type=str, help="put the name of output file")

args = parser.parse_args()
#print(args.page_size)
#print(args.num_pages)
#print(args.output)	
if args.num_pages > 0:
	results = client.get("nc67-uf89", limit = args.page_size*args.num_pages)
else: 
	results = client.get("nc67-uf89", limit = num_rows)

df = pd.DataFrame.from_dict(results)
df.to_json (args.output, orient='records', lines=True)
	

