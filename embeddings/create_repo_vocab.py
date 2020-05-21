from clean_text import clean_text
import os
import sys

repos_dir = sys.argv[1]
dest = sys.argv[2]

for repo_dir in os.listdir(repos_dir):
    full_path = os.path.join(repos_dir, repo_dir)
    if not os.path.isdir(full_path):
        continue
    dest_path = os.path.join(dest, repo_dir)
    with open(dest_path, 'w') as out_handle:
        total_read = 0
        for root, dirs, files in os.walk(full_path):
            for filename in files:
                f_full_path = os.path.join(root, filename)
                
                try:
                    with open(f_full_path) as handle:
                        everything = handle.read(100000) # read 1 mb
                        everything = ' '.join(clean_text(everything))
                        total_read += len(everything.encode('utf-8'))
                        
                        out_handle.write(everything)
                        out_handle.write(' ')

                        if total_read > 1000000:
                            break
                except:
                    pass

            if total_read > 1000000:
                break                
