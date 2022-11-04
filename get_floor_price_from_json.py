# This program imports a json file specified in the command line arguments and prints the floorprice.
# To make the json file, first run: get_collection_stats.py
# Run this program with the command: python get_floor_price_from_json.py [cslug]
# i.e: python get_floor_price_from_json.py metacard-by-fullsend



import sys
import json

collection = sys.argv[1]

folder_path = f'/Users/matt/Documents/nft/data/{collection}/{collection}.json'
floor_price = "floor_price"

f = open(folder_path)

data = json.load(f)

if floor_price in data:
    print(data[floor_price])
else:
    print("%s no floor price found")