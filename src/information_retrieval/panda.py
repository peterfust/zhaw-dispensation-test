import pandas as pd

# Series (1 dimension)
s = pd.Series([5, 10, 15, 20, 25])
print(s)
print("2. Element: " + str(s[1]))
print("2. - 3. Element: " + str(s[1:4]))

print('=====================================')
# Dataframes (2 dimension)

df1 = pd.DataFrame([5, 10, 15, 20, 25])  # aus Liste
print(df1)
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.date_range('2000-01-01', '2000-01-07'),
    'C': pd.Series(range(7), dtype='float32'),
    'D': pd.Categorical(['on', 'off', 'on', 'off', 'on', 'off', 'on']),
    'E': 'foo'})

print(df2)
print(df2['B'])
print(df2.head(2))
print(df2.columns)
print(df2.values)
print(df2.sort_index(axis=0, ascending=False))  # mit axis=1 sortieren nach Zeilen-Index
print(df2.sort_index(axis=1, ascending=False))  # mit axis=1 sortieren nach Spalten-Index
print(df2.sort_values(by='D', axis=0, ascending=False))  # Zeilen sortieren nach Spalte D
print(df2.loc[1:3, ['B','D']])  # Zeile 1-3, Spalte B und D


df = pd.read_json('./panda_bestellungen.json')
print(df)
df.drop_duplicates(inplace=True)
print(df)