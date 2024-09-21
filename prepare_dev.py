import pandas as pd
asnq = pd.read_csv("/Users/praju/Summer/ml/data/asnq/dev.tsv", sep='\t', names=['sentence1','sentence2','label'])  # format of run_glue.py
asnqNeg = asnq[asnq['label']==3].sample(frac=0.25)
asnqNeg.loc[:,'label'] = 0
asnqPos = asnq[asnq['label']==4]
asnqPos.loc[:,'label'] = 1
pd.concat([asnqNeg, asnqPos]).to_csv("dev.csv", index=False)