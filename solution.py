import pandas as pd
import timeit
import numpy as np
import jellyfish
import recordlinkage
import pdb 

df = pd.read_csv('data/test.csv',escapechar='\\')
df['first_name'] = df['first_name'].str.lower()
df['last_name'] = df['last_name'].str.lower()

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

def find_all_matches(first_df,second_df):
	index = recordlinkage.Pairs(first_df, second_df)
	links = index.full()
	fill = recordlinkage.Compare(links, first_df, second_df)

	fill.string('first_name', 'first_name', method='jaro', threshold=0.72)
	fill.string('last_name', 'last_name', method='jaro', threshold=0.83)

	return get_df_from_vector(fill.vectors,first_df,second_df)

def get_df_from_vector(result,first_df,second_df):
	correct = result[(result[0] == 1) & (result[1] == 1)]
	first_df_index = correct.index.labels[0]
	second_df_index = correct.index.labels[1]

	return first_df.iloc[first_df_index].append(second_df.iloc[second_df_index])

def spit_out(first_df,second_df,third_df):
	final_df = (find_all_matches(
	first_df,second_df).append(find_all_matches(
	first_df,third_df).append(find_all_matches(
	second_df,third_df)))).drop_duplicates().sort('first_name')

	return final_df

final = spit_out(df_1,df_2,df_3)
final.to_csv('data/results.csv', sep='\t')
