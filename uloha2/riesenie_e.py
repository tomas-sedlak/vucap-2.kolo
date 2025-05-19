import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načítanie dát
file_path = 'uloha2/SpotifySongs2023.csv'
df = pd.read_csv(file_path, encoding_errors="ignore")

# Prevod streams na číslo, ak je to možné
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
valid_df = df.dropna(subset=['streams'])

# Zoskupenie podľa artist(s)_name a výpočet celkového počtu streamov
artist_streams = valid_df.groupby('artist(s)_name')['streams'].sum().reset_index()

# Usporiadanie podľa streamov v klesajúcom poradí
artist_streams = artist_streams.sort_values('streams', ascending=False)

# Získanie top 10 najpopulárnejších umelcov
top_10_artists = artist_streams.head(10)

plt.figure(figsize=(8, 6))
sns.barplot(data=top_10_artists, x='artist(s)_name', y='streams', palette='rocket')
plt.title('Top 10 najpopulárnejších umelcov')
plt.xlabel('Umelec')
plt.ylabel('Počet streamov')
plt.xticks(rotation=30, ha='right')

plt.tight_layout()
plt.savefig('uloha2/obrazky/riesenie_e.png')
plt.show()