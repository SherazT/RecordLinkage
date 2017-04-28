import solution
import pandas as pd
import numpy as np
import pdb

df = pd.read_csv('data/test.csv',escapechar='\t')

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

expected_results = pd.read_csv('expected_results.csv',sep=',')

def test_spit_out():
	result = solution.spit_out(df_1,df_2,df_3)
	pdb.set_trace()



