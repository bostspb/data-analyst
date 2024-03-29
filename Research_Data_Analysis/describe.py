import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')
print(data.describe())