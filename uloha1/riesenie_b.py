import pandas as pd
import matplotlib.pyplot as plt

# Načítanie dát
path = 'uloha1/pohyby_lodi.xlsx'
df = pd.read_excel(path)
ship_ids = df['Ship_ID'].unique()

# Vykreslenie grafu pre každú loď
for ship_id in ship_ids:
    ship_data = df[df['Ship_ID'] == ship_id]
    plt.figure(figsize=(10, 8))
    plt.plot(ship_data['Longitude'], ship_data['Latitude'],
             marker='o', label=f'Loď {ship_id}')
    plt.xlabel('Zemepisná dĺžka')
    plt.ylabel('Zemepisná šírka')
    plt.title(f'Pohyb lode {ship_id} - 1. február 2025')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    filename = f'uloha1/pohyby_lodi/pohyb_lode_{ship_id}.png'
    plt.savefig(filename)
    plt.close()
    print(f'Uložený graf pre loď {ship_id}: {filename}')

# Graf všetkých lodí spolu
plt.figure(figsize=(12, 10))
colors = plt.get_cmap('tab10', len(ship_ids))
for idx, ship_id in enumerate(ship_ids):
    ship_data = df[df['Ship_ID'] == ship_id]
    plt.plot(ship_data['Longitude'], ship_data['Latitude'],
             marker='o', label=f'Loď {ship_id}', color=colors(idx))
plt.xlabel('Zemepisná dĺžka')
plt.ylabel('Zemepisná šírka')
plt.title('Pohyb všetkých lodí - 1. február 2025')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('uloha1/pohyby_lodi/pohyb_lodi.png')
plt.close() 
print('Uložený graf pre všetky lode: pohyb_lodi.png')