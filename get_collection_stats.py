# This program gets and saves the stats of a certain collection on opensea in a json file.
# Pass the desired cslug as a command line arguemnt
# python get_collection_stats.py [cslug]
# i.e: python get_collection_stats.py metacard-by-fullsend
# tutorial: https://www.youtube.com/watch?v=dzO2_uZ0zYk&ab_channel=JT4wardApps

import requests
import sys
import os
import json

cslug = sys.argv[1]

def get_collection_stats(collection_slug):
    url = f'https://api.opensea.io/api/v1/collection/{collection_slug}/stats'
    resp = requests.get(url)
    data = resp.json()
    stats = data['stats']
    return stats


if __name__ == '__main__':
    stats = get_collection_stats(cslug)
    folder_path = f'./data/{cslug}'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    stats_path = os.path.join(folder_path, f'{cslug}.json')
    json.dump(stats, open(stats_path, 'w'))
    print("done.")