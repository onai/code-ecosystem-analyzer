import requests
import sys

with open(sys.argv[1]) as handle:
    for new_line in handle:
            resp = requests.get(new_line.strip(), auth=(sys.argv[2], sys.argv[3]))
            for res in resp.json():
                print(res['archive_url'])
        
