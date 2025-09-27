from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

years = [2022, 2023, 2024]
months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
cleanDataFrames: Dict[str, pd.DataFrame] = {}

for year in years:
    for month in months:
        var_name = f"{month}{str(year)[-2:]}"
        # Exemplo de leitura (substitua pelo seu método de obtenção dos DataFrames)
        cleanDataFrames[var_name] = pd.read_csv(f"../Medium/data_cleaned/{year}/{month}/{var_name}.csv", sep=";")

# Contagem por mês
monthly_counts = {}
for key, df in cleanDataFrames.items():
    counts = df['ICAO Aeródromo Origem'].value_counts()
    monthly_counts[key] = counts

# Soma acumulada por empresa em todos os meses
total_counts = defaultdict(int)
for counts in monthly_counts.values():
    for company, qty in counts.items():
        total_counts[company] += qty

# Transformar dict em DataFrame
total_df = pd.DataFrame.from_dict(total_counts, orient='index', columns=['Total'])
total_df = total_df.sort_values('Total', ascending=False)

# Selecionar top N e criar "Outros"
n = 15
topN = total_df.head(n)
others_sum = total_df.iloc[n:].sum().values[0]

plot_df = topN.copy()
plot_df.loc['Outros'] = others_sum

# Plot
plt.figure(figsize=(14,8))
bars = plt.bar(plot_df.index, plot_df['Total'], color=sns.color_palette('viridis', 4), width=0.6)

# Adicionando valores no topo das barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 5, f'{int(height)}', ha='center', va='bottom', fontsize=11)

plt.title("Top 3 Aeroportos  + Outros (voos atrasados)", fontsize=14)
plt.ylabel("Quantidade de voos atrasados", fontsize=12)
plt.xlabel("Código ICAO do Aeroporto", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()