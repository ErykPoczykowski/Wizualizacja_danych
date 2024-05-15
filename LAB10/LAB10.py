import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(100))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# zad1
# df = pd.read_excel("imiona.xlsx")
# df_grouped = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(df_grouped)
# df_grouped.plot()
# plt.xticks(df['Rok'].unique())
# plt.xticks(rotation=90)
# plt.show()

# zad2
# df = pd.read_excel("imiona.xlsx")
# df_grouped = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(df_grouped)
# df_grouped.plot.bar()
# plt.show()

# zad 3
df = pd.read_excel("imiona.xlsx")
lata = df[df['Rok'] >= df['Rok'].max() - 4]
grupa_dzieci = lata.groupby('Plec').sum()
urodzenia = grupa_dzieci['Liczba'].sum()
grupa_dzieci['Procent'] = (grupa_dzieci['Liczba'] / urodzenia) * 100
plt.figure(figsize=(8, 6))
plt.pie(grupa_dzieci['Procent'], labels=grupa_dzieci.index, autopct='%1.1f%%', startangle=90)
plt.title('Procentowy udział urodzeń chłopców i dziewczynek\n w ostatnich 5 latach')
plt.axis('equal')
plt.show()

# zad 4
# df2 = pd.read_csv("zamowienia.csv", sep=';')
# df2_grouped = df2.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
# print(df2_grouped)
# df2_grouped.plot.bar()
# plt.show()




