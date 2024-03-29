import pandas as pd

data = pd.read_csv('visits.csv', sep='\t')

# Верификация данных
total_visits = data.shape[0]
print(f'Количество заездов: {total_visits}')
total_stations = len(data['id'].unique())
print(f'Количество АЗС: {total_stations}')
print(data['date_time'].min(), data['date_time'].max())
total_days = 7
station_visits_per_day = total_visits / total_stations / total_days
print(f'Количество заездов на АЗС в сутки: {station_visits_per_day}')
print(data['name'].value_counts().head(10))

# Фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')

# Считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')

stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
print(id_name.head())
print()

# Переименование столбцов
id_name.columns = ['name', 'count']
print(id_name.head())

# Объединение столбцов методами merge() и join()
station_stat_full = id_name.join(good_stations_stat)

# Считаем показатели сетей из показателей АЗС, а не усреднённые заезды на все АЗС сети
good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2, on='name')
print(final_stat)

# Диаграмма рассеяния
station_stat_full.plot(x='count', y='time_spent', kind='scatter', grid=True)

# Коэффициент корреляции Пирсона
print(station_stat_full['count'].corr(station_stat_full['time_spent']))

# station_stat_multi:
# среднее (не медиана) продолжительности заезда на АЗС;
# средняя доля быстрых заездов;
# средняя доля медленных заездов.
station_stat_multi = data.pivot_table(index='id', values=['time_spent', 'too_fast', 'too_slow'], aggfunc='mean')

# Матрица диаграмм рассеяния для station_stat_multi
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))

# Матрица корреляции
print(station_stat_multi.corr())

# Сравним корреляцию по исходным данным и по отфильтрованным чтобы наглядно увидеть -
# почему мы отсекли самые медленные заезды и самые быстрые.

station_stat_multi['good_time_spent'] = good_stations_stat['time_spent']
pd.plotting.scatter_matrix(station_stat_multi, figsize=(9, 9))
print(station_stat_multi.corr())
"""
Было (time_spent, too_fast) = 0.64 и (time_spent, too_slow) = 0.80
Стало (good_time_spent, too_fast) = 0.32 и (good_time_spent, too_slow) = 0.45
Коэффициенты снизились, влияние аномальных значений уменьшилось
"""


# Укрупняем группы
# Все мелкие сети объединим в группу `Другие`
big_nets_stat = final_stat.query('stations > 10')
station_stat_full['group_name'] = (
    station_stat_full['name']
    .where(station_stat_full['name'].isin(big_nets_stat.index), 'Другие')
)

stat_grouped = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count'])
)
stat_grouped.columns = ['time_spent', 'count']

# Круговая диаграмма
stat_grouped.plot(kind='pie', y='count', figsize=(8, 8))

good_data['group_name'] = good_data['name'].where(
    good_data['name'].isin(big_nets_stat.index),
    'Другие'
)
print(good_data.head())

# Гистограммы отдельно для каждой сети -
# вдруг на среднюю продолжительность заправки повлияли аномально короткие заезды.
for name, group_data in good_data.groupby('group_name'):
    print(group_data.plot(y='time_spent', title=name, kind='hist', bins=50, grid=True))

"""
У многих сетей АЗС явно обнаруживается аномальный пик на коротких заездах. 
Но в основном распределение имеет ожидаемую форму, а значит, медиана хорошо передаёт характерное время заправки. 
Мы выявили много долгих заправок в самых медленных сетях АЗС («Роза», «Календула», «Василёк», «Немезия»). 
Причём форма распределения достаточно плавная: не походит на явную аномалию в продолжительности заправки. 
"""