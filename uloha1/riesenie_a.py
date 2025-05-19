import pandas as pd

# Načítanie dát
path = 'uloha1/pohyby_lodi.xlsx'
df = pd.read_excel(path)

# Skontroluj zoradenie podľa Ship_ID a Timestamp
is_sorted = df.sort_values(['Ship_ID', 'Timestamp']).equals(df)
if is_sorted:
    print("Dáta sú správne zoradené podľa Ship_ID a Timestamp.")
else:
    print("Dáta NIE sú správne zoradené. Exportujem správne zoradený súbor ako pohyby_lodi_sorted.xlsx.")
    # Zoradíme a exportujeme
    sorted_df = df.sort_values(['Ship_ID', 'Timestamp']).reset_index(drop=True)
    sorted_df.to_excel('uloha1/pohyby_lodi_sorted.xlsx', index=False)
