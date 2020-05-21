from MulticoreTSNE import MulticoreTSNE as TSNE
from sklearn.cluster import KMeans
import numpy as np
import sys
import joblib

res = joblib.load(sys.argv[1])

embeddings = []
repo_names = []

for k, v in res.items():
    embeddings.append(v)
    repo_names.append(k)

embeddings = np.array(embeddings)

dimreds = TSNE(n_jobs=4).fit_transform(embeddings)

preds = KMeans(n_clusters=8).fit_predict(dimreds)

import matplotlib; matplotlib.use('Agg')
from matplotlib import pyplot as plt

for i in range(preds.max() + 1):
    plt.scatter(dimreds[np.where(preds==i)][:,0], dimreds[np.where(preds==i)][:,1], color='C' + str(i), label=str(i))
    #plt.scatter(dimreds[:,0], dimreds[:,1])

pred_names = {}

for i, p in enumerate(preds):
    if p in pred_names:
        pred_names[p].append(repo_names[i])
    else:
        pred_names[p] = [repo_names[i]]

plt.legend()
plt.savefig('repos.png')

for repo, names in pred_names.items():
    print(repo)
    print(names)
