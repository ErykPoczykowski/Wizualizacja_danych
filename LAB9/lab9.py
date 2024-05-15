import pandas as pd
import numpy as np
# zad 1 oraz 2
df = pd.read_excel("imiona.xlsx")
# print(df)

df_1 = df[df['Liczba']>1000]

df_2 = df[df['Imie']=='ERYK']

df_3 = df['Liczba'].sum()

df_4 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()

df_5 = df.groupby('Plec')['Liczba'].sum()

df_6 = df.sort_values(by='Rok', ascending=False).groupby(['Rok','Plec']).head(1)
# print(df_1)
# print(df_2)
# print(df_3)
# print(df_4)
# print(df_5)
# print(df_6)
# -------------------------
# zad 3
df2 = pd.read_csv('zamowienia.csv', sep=';')

df2_1 = df2['Sprzedawca'].unique()

df2_2 = df2.sort_values(by="Utarg", ascending=False).head(5)

df2_3 = df2.groupby("Sprzedawca").count()
# print(df2_1)
# print(df2_2)
print(df2_3)
