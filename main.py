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

client = Socrata(domain, app_token)
data_size = client.get(identifier, select='COUNT(*)')[0]
num_rows = int(str(data_size)[11:19])

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
    
    es.indices.put_mapping(
        index=index_name,
        doc_type=doc_type,
        body={
            doc_type: {
                "properties": {"fine_amount": {"type": "double"}, 
                "reduction_amount": {"type": "double"}, 
                "penalty_amount": {"type": "double"}, 
                "payment_amount": {"type": "double"}}
            }
        }
    )
    return es

es = create_and_update_index('parking_violation','violation')

i = 0
while i < num_pages:
    results = client.get(identifier, limit=page_size
    , offset=i*page_size)

    docks = results

    for dock in docks:
        try:
            dock["issue_date"] = str(dock["issue_date"])
            dock["issue_date"] = datetime.strptime(
                dock["issue_date"],"%m/%d/%Y")

            es = Elasticsearch()
            
            res = es.index(index='parking_violation'
            , doc_type='violation', body=dock)
            
            print(res['result'])

        except Exception:
            pass
    i += 1
