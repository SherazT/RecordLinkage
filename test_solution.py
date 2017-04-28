import solution
import pandas as pd
import numpy as np
import pandas.util.testing as pdt
import pdb

df = pd.read_csv('data/test_input.csv',escapechar='\\')
df['first_name'] = df['first_name'].str.lower()
df['last_name'] = df['last_name'].str.lower()

df_1 = df[df.source == 'source_1']
df_2 = df[df.source == 'source_2']
df_3 = df[df.source == 'source_3']

with open('data/expected_results.csv') as f:
    expected_results = pd.read_table(f, sep='\t', index_col=0)

def test_spit_out():
	result = solution.spit_out(df_1,df_2,df_3)
	pdt.assert_frame_equal(result,expected_results)

