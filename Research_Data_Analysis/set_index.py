"""
Как добавлять столбец из одного датафрейма к другому
"""
import pandas as pd

df1 = pd.DataFrame({'a': [1, 2, 3, 3, 3],
                    'b': ['Q', 'R', 'S', 'T', 'U']})
df2 = pd.DataFrame({'c': [3, 4, 5, 6, 7],
                    'd': ['V', 'W', 'X', 'Y', 'Z'],
                    'e': [3, 3, 3, 3, 3]})
df2.set_index('c', inplace=True)
print(df1)
print()
print(df2)
df1['new'] = df2['d']
print()
print(df1)
