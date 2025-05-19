import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načítanie dát
file_path = 'uloha2/SpotifySongs2023.csv'
df = pd.read_csv(file_path, encoding_errors="ignore")

# Prevod danceability na číslo
df['danceability_%'] = pd.to_numeric(df['danceability_%'], errors='coerce')
valid_df = df.dropna(subset=['danceability_%', 'mode'])

# Definovanie vysokého prahu danceability (75. percentil)
danceability_threshold = valid_df['danceability_%'].quantile(0.75)

# Filtrovanie piesní s vysokou danceability
high_danceability_songs = valid_df[valid_df['danceability_%'] >= danceability_threshold]

# Počítanie piesní podľa módu
mode_counts = high_danceability_songs['mode'].value_counts()

# Výpočet percentuálneho zastúpenia
mode_percentages = (mode_counts / len(high_danceability_songs)) * 100

# Vytvorenie grafu
plt.figure(figsize=(10, 6))
plt.pie(mode_counts.values, labels=mode_counts.index, autopct='%1.1f%%')
plt.title('Rozdelenie módov v piesňach s vysokou danceability')

plt.tight_layout()
plt.savefig('uloha2/obrazky/riesenie_f.png')
plt.show()
