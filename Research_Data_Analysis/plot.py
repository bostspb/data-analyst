"""
histtype (от англ. the type of histogram — «тип гистограммы»). В параметре указывают тип гистограммы,
по умолчанию — это столбчатая (закрашенная). Значение step (пер. «шаг») чертит только линию.

linewidth (от англ. width of line — «толщина линии»). Задаёт толщину линии графика в пикселях.

alpha (от термина «альфа-канал»). Назначает густоту закраски линии. 1 — это 100%-я закраска;
0 — прозрачная линия. С параметром 0.7 линии чуть прозрачны, так виднее их пересечения.

label (пер. «ярлык», «этикетка»). Название линии.

ax (от англ. axis — «ось»). Метод plot() возвращает оси, на которых был построен график.
Чтобы обе гистограммы расположились на одном графике, сохраним оси первого графика в переменной ax,
а затем передадим её значение параметру ax второго plot(). Так, сохранив оси одной гистограммы и
построив вторую на осях первой, мы объединили два графика.

legend (пер. «легенда»). Выводит легенду — список условных обозначений на графике.
На графике вы можете найти её в верхнем правом углу.
"""
import pandas as pd

median_station_stat = data.pivot_table(
    index='id', values='time_spent', aggfunc='median'
)
good_stations_stat = good_data.pivot_table(
    index='id', values='time_spent', aggfunc='median'
)

ax = median_station_stat.plot(
    kind='hist',
    y='time_spent',
    histtype='step',
    range=(0, 500),
    bins=25,
    linewidth=5,
    alpha=0.7,
    label='raw',
)
good_stations_stat.plot(
    kind='hist',
    y='time_spent',
    histtype='step',
    range=(0, 500),
    bins=25,
    linewidth=5,
    alpha=0.7,
    label='filtered',
    ax=ax,
    grid=True,
    legend=True,
)

# ---------------------------------------

# Диаграмма рассеяния
hw = pd.read_csv('hwa.csv', sep=';')
"""
         height       weight
0    167.089607    51.253398
1    181.648633    61.910639
2    176.272800    69.413002
3    173.270164    64.563337
4    172.181037    65.453165 
"""
hw.plot(x='height', y='weight', kind='scatter')  # кружки
hw.plot(x='height', y='weight', kind='scatter', alpha=0.03)  # прозрачность для наглядности скопления кружков
# цвет для наглядности - kind='hexbin' - частотность видна по насыщенности цвета
hw.plot(x='height', y='weight', kind='hexbin', gridsize=20, figsize=(8, 6), sharex=False, grid=True)

# ---------------------------------------

# Круговая диаграмма
stat_grouped.plot(kind='pie', y='count', figsize=(8, 8))
