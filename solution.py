import pandas as pd
import numpy as np
import jellyfish
import recordlinkage
import pdb #byebug for python --> pdb.set_trace()

df = pd.read_csv('people.csv',escapechar='\\')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def s1_s2():
	#-----------------------compare source 1 and source 2-----------------
	index = recordlinkage.Pairs(df_1, df_2)
	links = index.full()
	fill = recordlinkage.Compare(links, df_1, df_2)

	fill.string('first_name', 'first_name', method='jarowinkler',threshold=0.70)
	fill.string('last_name', 'last_name', method='jarowinkler', threshold=0.70)

	result = fill.vectors
	correct = result[(result[0] == 1) & (result[1] == 1)]

	first_df_index = remove_duplicates(correct.index.labels[0])
	second_df_index = remove_duplicates(correct.index.labels[1])

	return df_1.iloc[first_df_index].append(df_2.iloc[second_df_index])
	
def s1_s3():
	#-----------------------compare source 1 and source 3-----------------
	index = recordlinkage.Pairs(df_1, df_3)
	links = index.full()
	fill = recordlinkage.Compare(links, df_1, df_3)

	fill.string('first_name', 'first_name', method='jarowinkler',threshold=0.70)
	fill.string('last_name', 'last_name', method='jarowinkler', threshold=0.70)

	result = fill.vectors
	correct = result[(result[0] == 1) & (result[1] == 1)]

	first_df_index = remove_duplicates(correct.index.labels[0])
	second_df_index = remove_duplicates(correct.index.labels[1])

	return df_1.iloc[first_df_index].append(df_3.iloc[second_df_index])

def s2_s3():
	#-----------------------compare source 2 and source 3-----------------
	index = recordlinkage.Pairs(df_2, df_3)
	links = index.full()
	fill = recordlinkage.Compare(links, df_2, df_3)

	fill.string('first_name', 'first_name', method='jarowinkler',threshold=0.70)
	fill.string('last_name', 'last_name', method='jarowinkler', threshold=0.70)

	result = fill.vectors
	correct = result[(result[0] == 1) & (result[1] == 1)]

	first_df_index = remove_duplicates(correct.index.labels[0])
	second_df_index = remove_duplicates(correct.index.labels[1])

	return df_2.iloc[first_df_index].append(df_3.iloc[second_df_index])
	

final = s1_s2().append(s1_s3().append(s2_s3())).drop_duplicates()

pdb.set_trace()

# if __name__ == "__main__":
#     main()