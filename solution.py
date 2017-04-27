import pandas as pd
import numpy as np
import jellyfish
import recordlinkage
import pdb #byebug for python --> pdb.set_trace()


df = pd.read_csv('test.csv',escapechar='\\')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

#-----------------------compare source 1 and source 2-----------------
index = recordlinkage.Pairs(df_1, df_2)
links = index.full()
fill = recordlinkage.Compare(links, df_1, df_2)

fill.string('first_name', 'first_name', method='jarowinkler',threshold=0.70)
fill.string('last_name', 'last_name', method='jarowinkler', threshold=0.70)

result = fill.vectors
correct = result[(result[0] == 1) & (result[1] == 1)]

first_df_index = correct.index.tolist()[0][0]
second_df_index = correct.index.tolist()[0][1]


pdb.set_trace()


# if __name__ == "__main__":
#     main()