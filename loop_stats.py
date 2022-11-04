
import requests
import sys
import os
import json

cslug = sys.argv[1]
count = 0

def get_collection_stats(collection_slug):
    url = f'https://api.opensea.io/api/v1/collection/{collection_slug}/stats'
    resp = requests.get(url)
    data = resp.json()
    stats = data['stats']
    return stats

def get_floor_price(collection):
    folder_path = f'/Users/matt/Documents/nft/data/{collection}/{collection}.json'
    floor_price = "floor_price"

    f = open(folder_path)

    data = json.load(f)

    if floor_price in data:
        print(data[floor_price])
    else:
        print("%s no floor price found")

while 1:
    if __name__ == '__main__':
        stats = get_collection_stats(cslug)
        folder_path = f'./data/{cslug}'
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        stats_path = os.path.join(folder_path, f'{cslug}.json')
        json.dump(stats, open(stats_path, 'w'))
        
        #print the floor price
        get_floor_price(cslug)
        print("number ", count)
        count += 1