import sys
import json

with open(sys.argv[1]) as handle:
    for new_line in handle:
        uniqs = set(json.loads(new_line))
        for module in uniqs:
            print(module.split('.')[0])
