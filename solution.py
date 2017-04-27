import pandas as pd
import numpy as np
import jellyfish
import recordlinkage
import pdb #byebug for python --> pdb.set_trace()

df = pd.read_csv('test.csv',escapechar='\\')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

def find_all_matches(first_df,second_df):
	index = recordlinkage.Pairs(first_df, second_df)
	links = index.full()
	fill = recordlinkage.Compare(links, first_df, second_df)

	fill.string('first_name', 'first_name', method='jarowinkler',threshold=0.70)
	fill.string('last_name', 'last_name', method='jarowinkler', threshold=0.70)

	result = fill.vectors
	correct = result[(result[0] == 1) & (result[1] == 1)]

	first_df_index = correct.index.labels[0]
	second_df_index = correct.index.labels[1]

	return first_df.iloc[first_df_index].append(second_df.iloc[second_df_index])
	

	

final = find_all_matches(df_1,df_2).append(find_all_matches(df_1,df_3).append(find_all_matches(df_2,df_3))).drop_duplicates()

final.to_csv('results.csv', sep='\t')

# pdb.set_trace()

# if __name__ == "__main__":
#     main()