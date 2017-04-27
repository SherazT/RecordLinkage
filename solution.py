import pandas as pd
import numpy as np
import jellyfish
import recordlinkage
from nameparser import HumanName
import pdb #byebug for python --> pdb.set_trace()


df = pd.read_csv('test.csv',escapechar='\\')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

index = recordlinkage.Pairs(df_1, df_2)

links = index.full()

fill = recordlinkage.Compare(links, df_1, df_2)

pdb.set_trace()


fill.string('first_name', 'first_name', method='jarowinkler')
fill.string('last_name', 'last_name', method='jarowinkler')


ecm = recordlinkage.ECMClassifier()
ecm.learn(fill.vectors)


pdb.set_trace()


# if __name__ == "__main__":
#     main()