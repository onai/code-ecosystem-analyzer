from fastText import load_model
import sys
import os
import joblib

repos = sys.argv[1]
model_f = sys.argv[2]
model = load_model(model_f)

res = {}

for repo_voc in os.listdir(repos):
    full_path = os.path.join(repos, repo_voc)
    print(full_path)
    with open(full_path) as handle:
        sent = handle.read()
        v = model.get_sentence_vector(sent)
        res[repo_voc] = v

joblib.dump(res, 'repo_vectors')
