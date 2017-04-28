import pandas as pd
import timeit
import numpy as np
import jellyfish
import recordlinkage
from recordlinkage.datasets import load_krebsregister
import pdb 

df = pd.read_csv('cross.csv',escapechar='\\')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

def find_all_matches(first_df, second_df):
	index = recordlinkage.Pairs(first_df, second_df)
	# links = index.random(n=0)
	links = index.full()
	fill = recordlinkage.Compare(links, first_df, second_df)

	fill.string('first_name', 'first_name', method='jaro') #threshold=0.72
	fill.string('last_name', 'last_name', method='jaro') #threshold=0.82
	comp_vector = ml_model(fill.vectors)
	correct = comp_vector[(comp_vector[0] == 1) & (comp_vector[1] == 1)]
	first_df_index = correct.index.labels[0]
	second_df_index = correct.index.labels[1]

	return first_df.iloc[first_df_index].append(second_df.iloc[second_df_index])

def ml_model(comp_vector):
	train_input = load_krebsregister(missing_values=0)
	train_data = train_input[0][0:5000]
	train_result = train_input[1][0:5000]

	true_linkage = pd.Series(train_data, index=pd.MultiIndex(train_result))

	logrg = recordlinkage.LogisticRegressionClassifier()
	logrg.learn(compare.vectors[true_linkage.index], true_linkage)
	
	return logrg.predict(comp_vector)

def spit_out():
	final = (find_all_matches(df_1,df_2).append(find_all_matches(df_1,df_3).append(find_all_matches(df_2,df_3)))).drop_duplicates().sort('first_name')
	final.to_csv('results.csv', sep='\t')

# print(timeit.timeit(spit_out))

spit_out()