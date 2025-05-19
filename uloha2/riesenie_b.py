import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načítanie dát
file_path = 'uloha2/SpotifySongs2023.csv'
df = pd.read_csv(file_path, encoding_errors="ignore")


# Vybrané kvantitatívne atribúty
attributes = ['streams', 'bpm', 'danceability_%']

plt.figure(figsize=(18, 5))

for i, attr in enumerate(attributes):
    plt.subplot(1, 3, i + 1)
    data = pd.to_numeric(df[attr], errors='coerce').dropna()
    sns.kdeplot(data, fill=True, label=attr)
    plt.title(f'Hustotný graf: {attr}')
    plt.xlabel(attr)
    plt.ylabel('Hustota')
    plt.legend()

plt.tight_layout()
plt.savefig('uloha2/obrazky/riesenie_b.png')
plt.show()