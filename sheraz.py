import recordlinkage
from recordlinkage.datasets import load_febrl1

dfA = load_febrl1()

# Indexation step
pcl = recordlinkage.Pairs(dfA)
pairs = pcl.block('given_name')

# Comparison step
compare_cl = recordlinkage.Compare(pairs, dfA, dfA)

compare_cl.exact('given_name', 'given_name', name='given_name')
compare_cl.string('surname', 'surname', method='jarowinkler', threshold=0.85, name='surname')
compare_cl.exact('date_of_birth', 'date_of_birth', name='date_of_birth')
compare_cl.exact('suburb', 'suburb', name='suburb')
compare_cl.exact('state', 'state', name='state')
compare_cl.string('address_1', 'address_1', threshold=0.85, name='address_1');

# Classification step
matches = compare_cl.vectors[compare_cl.vectors.sum(axis=1) > 3]
print(compare_cl)