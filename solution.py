import pandas as pd
import numpy as np
import csv
import pdb #byebug for python --> pdb.set_trace()

# with open('people.csv', newline='') as csvfile:
# 	file = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in file:
# 		pdb.set_trace()		

df = pd.read_csv('test.csv',escapechar='\\', encoding='utf-8')

pdb.set_trace()