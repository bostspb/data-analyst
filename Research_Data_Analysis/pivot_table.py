"""
index — столбец, значения которого становятся названиями строк (индексом), т.е. по этому полю идет группировка;
columns — столбец, значения которого становятся названиями столбцов сводной таблицы;
values — значения, по которым вы хотите увидеть сводную таблицу (по ним считается агрегат);
aggfunc — агрегат, применяемая к values, по умолчанию считается среднее арифметическое.
"""
import pandas as pd

data = pd.read_csv('visits.csv', sep='\t')
print(data.head())
print(data.info())
stat = data.pivot_table(index='name', values='time_spent')
print(stat)

