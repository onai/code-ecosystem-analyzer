import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys

f = sys.argv[1]

rows = []

with open(f) as handle:
    rank = 1
    for new_line in handle:
        print(new_line)
        cnt, item = new_line.strip().split()
        cnt = int(cnt)
        rows.append([rank, cnt])
        rank += 1

arr = np.array(rows)
log_log = np.log(arr)

plt.scatter(log_log[:,0], log_log[:,1])
plt.xlabel('log(rank)')
plt.ylabel('log(frequency)')
plt.title('file-level log-log scale plot of package frequencies')
plt.savefig('chart.png')
