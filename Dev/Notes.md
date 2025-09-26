# 1️⃣ Leitura e escrita

## `.read_csv(path, sep=";", parse_dates=[...], dtype={...})`
Lê um arquivo CSV e carrega como DataFrame
> sep: separador de colunas, parse_dates: converte colunas em datetime, dtype: força tipos

## `.to_csv(path, index=False)`
Salva o DataFrame em CSV
> index=False evita salvar o índice do DataFrame

# 2️⃣ Visualização rápida

## `.head(n)`
Mostra as n primeiras linhas (default n=5)

## `.tail(n)`
Mostra as n últimas linhas

## `.sample(n)`
Mostra n linhas aleatórias

## `.info()`
Mostra colunas, tipos de dados, quantidade de valores não nulos

## `.describe()`
Estatísticas descritivas de colunas numéricas (mean, std, min, max, quartis)

## `.nunique()`
Mostra número de valores únicos por coluna

## `.value_counts()`
Contagem de frequência de cada valor em uma série/coluna

## `len(n)`
Mostra o número de linhas do DataFrame

# 3️⃣ Seleção e filtragem

## `df["coluna"]`
Seleciona uma coluna (retorna Series)

## `df[["col1", "col2"]]`
Seleciona múltiplas colunas

## `df.iloc[linhas, colunas]`
Seleção por índice posicional (inteiro)

## `df.loc[linhas, colunas]`
Seleção por rótulo (nomes de colunas/linhas)

## `df[df["coluna"] > 100]`
Filtra linhas baseado em condição

# 4️⃣ Limpeza e preenchimento

## `.isnull()`
Retorna um DataFrame booleano indicando valores nulos

## `.notnull()`
Retorna booleano de não nulos
## `.dropna(subset=[...], inplace=False)`
Remove linhas com valores nulos em colunas especificadas

## `.fillna(valor, inplace=False)`
Substitui valores nulos por valor especificado (ex: 0, média, "Desconhecido")

## `.drop(columns=[...], inplace=False)`
Remove colunas indesejadas

# `.astype(tipo)`
Converte coluna(s) para outro tipo (str, int, float, datetime)

# 5️⃣ Operações em colunas

## `df["nova_coluna"] = df["col1"] - df["col2"]`
Cria nova coluna com operação entre colunas

## ...
```python
df["coluna"].str.upper()
df["coluna"].str.strip()
df["coluna"].str.replace("A", "B")
```
Operações em strings

# 6️⃣ Agrupamento e resumo

## `grouped = df.groupby("coluna")["outra_coluna"].mean()`
Agrupa por coluna e calcula média da outra
