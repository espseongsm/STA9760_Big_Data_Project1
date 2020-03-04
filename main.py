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
data_size = client.get(identifier, select='COUNT(*)')[0]
num_rows = int(str(data_size)[11:19])

#def main():
parser = argparse.ArgumentParser()#(usage="main.py --page_size=the_number_of_rows_in_a_page --num_pages=number_of_pages --output=filename", description="put the parameters")
	
parser.add_argument('--page_size', type=int, default=1000, help="put the page size")
parser.add_argument('--num_pages', type=int, default=0, help="put the number of pages")
parser.add_argument('--output', type=str, default='results.json', help="put the name of output file")

args = parser.parse_args()
#print(args.page_size)
#print(args.num_pages)
#print(args.output)	

if args.num_pages == 0:
	results = client.get("nc67-uf89", limit = num_rows)
else:
	results = client.get("nc67-uf89", limit = args.page_size*args.num_pages)

df = pd.DataFrame.from_dict(results)
df.to_json (args.output, orient='records', lines=True)
	

