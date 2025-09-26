import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Supondo que você tenha seu dict de DataFrames:
# dataFrames['jan22'], dataFrames['fev22'], ...

# 1️⃣ Contagem por mês
monthly_counts = {}
for key, df in dataFrames.items():
    counts = df['ICAO Empresa Aérea'].value_counts()
    monthly_counts[key] = counts

# 2️⃣ Soma acumulada por empresa em todos os meses
total_counts = defaultdict(int)
for counts in monthly_counts.values():
    for company, qty in counts.items():
        total_counts[company] += qty

# Converter para DataFrame para facilitar plot
total_df = pd.DataFrame.from_dict(total_counts, orient='index', columns=['Total'])
total_df = total_df.sort_values('Total', ascending=False)

# 3️⃣ Plotando os 10 maiores
top10 = total_df.head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top10.index, y=top10['Total'], palette='viridis')
plt.title("Top 10 empresas aéreas com mais registros de voos atrasados")
plt.xlabel("Código ICAO da Empresa Aérea")
plt.ylabel("Quantidade de voos atrasados")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
