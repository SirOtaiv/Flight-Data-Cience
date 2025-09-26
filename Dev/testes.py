import pandas as pd

df_test = pd.read_csv("./data/data_teste.csv", sep=";", skiprows=1, nrows=5)
print(df_test.columns.tolist())

# jan22 = pd.read_csv("../Origin/2022/Janeiro/VRA_Janeiro_20221.csv", sep=";")
# print(jan22.head())

# Aplicando filtro de valores vazios, nulos, inexistêntes em Datas
# filteredDataFrameObject = dataFrameObject.dropna(subset=["Partida Prevista", "Partida Real", "Chegada Prevista", "Chegada Real"])
