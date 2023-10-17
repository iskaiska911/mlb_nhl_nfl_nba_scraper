import json
import datetime
import requests
from loguru import logger as log

def post_products_mlb(base_url,products_formatted):
    filename=base_url+str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")+'.json')
    with open(filename, 'w') as f:
        json.dump(products_formatted, f)
