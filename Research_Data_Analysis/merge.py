import pandas as pd

first_pupil_df = pd.DataFrame({
    'author': ['Фонвизин', 'Грибоедов', 'Пушкин', 'Гоголь', 'Лермонтов'],
    'literary_work': ['Недоросль', 'Горе от ума', 'Капитанская дочка', 'Ревизор', 'Мцыри']
})
second_pupil_df = pd.DataFrame({
    'author': ['Пушкин', 'Гоголь','Лермонтов', 'Островский', 'Тургенев'],
    'literary_work': ['Евгений Онегин', 'Мёртвые души', 'Герой нашего времени', 'Гроза', 'Отцы и дети']
})
print(first_pupil_df)
print()
print(second_pupil_df)

# название столбца, по которому объединять, передают в параметре on
first_pupil_df.merge(second_pupil_df, on='author')  # inner

first_pupil_df.merge(second_pupil_df, on='author', how='outer')

first_pupil_df.merge(second_pupil_df, on='author', how='left')

first_pupil_df.merge(second_pupil_df, on='author', how='left', suffixes=('_записал первый', '_записал второй'))