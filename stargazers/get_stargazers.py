import requests
import sys

uname = sys.argv[1]
passwd = sys.argv[2]

with open(sys.argv[1]) as handle:
    for url in handle:
        url = url.strip()
        for i in range(1000):
            pg_url = '?page=' + str(i)
            the_url = url + pg_url
            
            req = requests.get(the_url, auth=(uname, passwd))
            try:
                for result in req.json():
                    print(result['repos_url'])
            except:
                break
