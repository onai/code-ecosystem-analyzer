import sys

with open(sys.argv[1]) as handle:
    for new_line in handle:
        dest = new_line.split('/')[4] + '_' + new_line.split('/')[5] + '.zip'
        #print('curl -Ls -I -o /dev/null -w \'%{url_effective}\\n\' ' + new_line.strip())
        print('curl -L --user ' + sys.argv[2] + ':' + sys.argv[3] + ' ' + new_line.strip() + ' -o ' + dest)
