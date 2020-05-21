import sys

with open(sys.argv[1]) as handle:
    for new_line in handle:
        print(new_line.split('.')[0].strip())
