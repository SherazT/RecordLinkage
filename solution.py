import pandas as pd
import numpy as np
import recordlinkage
import pdb #byebug for python --> pdb.set_trace()

# with open('people.csv', newline='') as csvfile:
# 	file = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in file:
# 		pdb.set_trace()		

df = pd.read_csv('test.csv',escapechar='\\')

df_1 = df[df.source == ' source_1']
df_2 = df[df.source == ' source_2']
df_3 = df[df.source == ' source_3']

# index = recordlinkage.Index(df_1, df_2)

# candidate_links = index.block('last_name')


pdb.set_trace()


# if __name__ == "__main__":
#     main()