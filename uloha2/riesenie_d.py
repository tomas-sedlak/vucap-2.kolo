import pandas as pd

# Načítanie dát
file_path = 'uloha2/SpotifySongs2023.csv'
df = pd.read_csv(file_path, encoding_errors="ignore")

missing_data = df.isnull().sum()
print("Hodnoty, ktore su null:")
for column, count in missing_data[missing_data > 0].items():
    print(f"{column}: {count} chýbajúcich hodnôt")