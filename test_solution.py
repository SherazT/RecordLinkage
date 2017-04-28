import solution
import pandas as pd
import numpy as np
import pandas.util.testing as pdt
import pdb

with open('data/expected_results.csv') as f:
    expected_results = pd.read_table(f, sep='\t', index_col=0)

def test_spit_out():
	df_1,df_2,df_3 = solution.import_file('data/test_input.csv')
	result = solution.spit_out(df_1,df_2,df_3)
	pdt.assert_frame_equal(result,expected_results)

