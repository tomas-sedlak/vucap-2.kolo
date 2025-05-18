import pandas as pd
import matplotlib.pyplot as plt

# Načítanie dát
file_path = 'uloha2/SpotifySongs2023.csv'
df = pd.read_csv(file_path, encoding='cp1252')

# Vybrané kvalitatívne atribúty
attributes = ['mode', 'key']

plt.figure(figsize=(14, 5))

for i, attr in enumerate(attributes):
    plt.subplot(1, 2, i + 1)
    value_counts = df[attr].value_counts(dropna=False)
    value_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title(f'Početnosti hodnôt atribútu: {attr}')
    plt.xlabel(attr)
    plt.ylabel('Počet výskytov')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('uloha2/obrazky/riesenie_c.png')
plt.show()