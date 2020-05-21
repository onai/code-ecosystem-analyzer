import sys

with open(sys.argv[1]) as handle:
    for new_line in handle:
        new_line = new_line.strip()
        url = new_line.replace('{archive_format}', 'zipball')
        url = url.replace('{/ref}', '')
        print(url)
