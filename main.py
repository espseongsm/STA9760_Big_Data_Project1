from sodapy import Socrata
import sys
import argparse
import json
import requests
import os
import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch
from datetime import datetime
from time import sleep
from math import ceil


domain = "data.cityofnewyork.us"
app_token = os.environ['APP_KEY']
identifier = "nc67-uf89"

# if __name__ == "__main__":

client = Socrata(domain, app_token)
data_size = client.get(identifier, select='COUNT(*)')[0]
num_rows = int(str(data_size)[11:19])

# def main():
# (usage="main.py --page_size=the_number_of_rows_in_a_page --num_pages=number_of_pages --output=filename", description="put the parameters")
parser = argparse.ArgumentParser()

parser.add_argument('--page_size', type=int, default=1000,
                    help="put the page size")
parser.add_argument('--num_pages', type=int, default=0,
                    help="put the number of pages")
parser.add_argument('--output', type=str, default="results.json",
                    help="put the name of output file")

args = parser.parse_args()

if args.num_pages == 0:
    page_size = args.page_size
    num_pages = ceil(num_rows/page_size)

else:
    page_size = args.page_size
    num_pages = args.num_pages

def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.delete(index=index_name)
        es.indices.create(index=index_name)
    except Exception:
        pass

    return es

es = create_and_update_index('parking-violation',
     'violation')

i = 0
while i < num_pages:
    results = client.get(identifier, limit=page_size
    , offset=i*page_size)

    # Step 1: create an elastic search "index" to store data
    print(4)

    # Step 2: fetch bike data from the internets
    docks = results
    print(7)
        
    # Step 3: Push data into the elastic search

    for dock in docks:
        dock["issue_date"] = str(dock["issue_date"])
        dock["issue_date"] = datetime.strptime(
            dock["issue_date"],"%m/%d/%Y")
        print(8)
        es = Elasticsearch()
        print(9)
        res = es.index(index='parking-violation'
        , doc_type='violation', body=dock)
        print(10)
        print(res['result'])
    i += 1
