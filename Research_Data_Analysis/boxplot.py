"""
Нарисуйте диаграмму размаха для data, ограничив диапазон по вертикали значениями -100 и 1000.
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/datasets/visits.csv', sep='\t')
data.boxplot()
plt.ylim(-100, 1000)
