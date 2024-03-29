import pandas as pd

df = pd.DataFrame(
    {
        'From': [
            'Moscow',
            'Moscow',
            'St. Petersburg',
            'St. Petersburg',
            'St. Petersburg',
        ],
        'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
        'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [21032, 19250, 19301, 20168, 31425],
        'Date_From': [
            '01.07.19',
            '01.07.19',
            '04.07.2019',
            '03.07.2019',
            '05.07.2019',
        ],
        'Date_To': [
            '07.07.19',
            '07.07.19',
            '10.07.2019',
            '09.07.2019',
            '11.07.2019',
        ],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
    }
)
df.query('To == "Barcelona"')
df.query('Travel_time_from < 2 * Travel_time_to ')
df.query('Travel_time_from < Travel_time_to.mean()')

maximum_price = 20000
df.query('Price <= @maximum_price')


"""
Выберите строки, где Airline равно Belavia, S7 или Rossiya, 
при этом Travel_time_from меньше переменной под названием max_time. 
Напечатайте полученную выборку на экране.
"""
max_time = 300
print(df.query('Airline in ["Belavia", "S7", "Rossiya"] and Travel_time_from < @max_time'))


# -----------------------------------------------------

our_series = pd.Series([10, 11, 12])
df = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
# строим срез, в котором значения столбца a равны значениям Series, но не их индексам
print(df.query('a in @our_series'))
# строим срез, в котором значения столбца a равны индексам Series, т. е. 0, 1 или 2
print(df.query('a in @our_series.index'))


# -----------------------------------------------------

our_dict = {0: 10, 1: 11, 2: 12}
df = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
# строим срез, в котором значения столбца a равны ключам словаря
print(df.query('a in @our_dict'))


# -----------------------------------------------------

our_list = [1, 2, 3]
df = pd.DataFrame({
    'a': [2, 3, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
# строим срез, в котором значения столбца `a` равны элементам списка `our_list`
print(df.query('a in @our_list'))


# -----------------------------------------------------

df = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
our_df = pd.DataFrame({
    'a1': [2, 4, 6],
    'b1': [3, 2, 2],
    'c1': ['A', 'B', 'C']
})
# строим срез, в котором значения столбца b равны значениям столбца b1 датафрейма our_df
print(df.query('b in @our_df.b1'))


