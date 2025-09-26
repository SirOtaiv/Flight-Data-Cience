from typing import Dict
import pandas as pd
import os

from steps.data_cleaning import cleanig_data

# Definindo anos e meses para leitura dos CSVs
years = [2022, 2023, 2024]
months = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Dicionários para armazenar os DataFrames lidos e limpos
dataFrames: Dict[str, pd.DataFrame] = {}
copyDataFrames: Dict[str, pd.DataFrame] = {}

# Pasta base onde os CSVs limpos serão salvos
output_base = "./data_cleaned/"

print("Iniciando o pipeline de leitura, limpeza e salvamento dos dados...")

# Definindo loops de leitura dos meses por anos
for year in years:
    for month in months:

        # Definindo nome da chave de cada DataFrame
        var_name = f"{month[:3]}{str(year)[-2:]}"
        
        # Lendo os arquivos CSV
        temp_df = pd.read_csv(
            f"./data/{year}/{month}/vra_{month}_{year}.csv",
            sep=";",
            skiprows=1,
            parse_dates=[
                "Partida Prevista", 
                "Partida Real", 
                "Chegada Prevista", 
                "Chegada Real"
            ],
            dtype={
                "ICAO Empresa Aérea": "string",
                "Número Voo": "string",
                "Código Autorização (DI)": "string",
                "Código Tipo Linha": "string",
                "ICAO Aeródromo Origem": "string",
                "ICAO Aeródromo Destino": "string",
                "Situação Voo": "string",
                "Código Justificativa": "string"
            })
        
        # Adicionando os DataFrames em uma lista
        dataFrames[var_name] = temp_df
        print(f"Arquivo {var_name} lido com sucesso!")

# Limpando dataFrames
for dfs in dataFrames:
    copyDataFrames[dfs] = cleanig_data(dataFrames[dfs].copy())
    print(f"DataFrame {dfs} limpo com sucesso!")

# Salvando os DataFrames limpos em CSVs organizados por ano e mês
for key, df in copyDataFrames.items():
    # Extrair ano e mês da chave
    month_str = key[:3]
    year_str = "20" + key[3:]

    # Criar a pasta do ano
    year_folder = os.path.join(output_base, year_str)
    os.makedirs(year_folder, exist_ok=True)

    # Criar a pasta do mês dentro do ano
    month_folder = os.path.join(year_folder, month_str)
    os.makedirs(month_folder, exist_ok=True)

    # Caminho final do arquivo CSV
    file_path = os.path.join(month_folder, f"{key}.csv")

    # Salvar o CSV
    df.to_csv(file_path, index=False, sep=";")

    print(f"DataFrame {key} salvo com sucesso em {file_path}!")

print("Todos os DataFrames foram salvos por ano e mês!")