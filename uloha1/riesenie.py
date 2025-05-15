import pandas as pd
import matplotlib.pyplot as plt
from geopy.distance import geodesic

# a) Načítanie dát a kontrola zoradenia
df = pd.read_excel('uloha1/pohyby_lodi.xlsx')

# Skontroluj zoradenie podľa Ship_ID a Timestamp
is_sorted = df.sort_values(['Ship_ID', 'Timestamp']).equals(df)
print("Dáta sú správne zoradené podľa Ship_ID a Timestamp:" if is_sorted else "Dáta NIE sú správne zoradené.")

# Ak nie sú zoradené, zoradíme ich
df = df.sort_values(['Ship_ID', 'Timestamp']).reset_index(drop=True)

# b) Vizualizácia pohybu lodí na mape
plt.figure(figsize=(10, 8))
ship_ids = df['Ship_ID'].unique()
colors = plt.cm.get_cmap('tab10', len(ship_ids))

for idx, ship_id in enumerate(ship_ids):
    ship_data = df[df['Ship_ID'] == ship_id]
    plt.plot(ship_data['Longitude'], ship_data['Latitude'],
             marker='o', label=f'Loď {ship_id}', color=colors(idx))

plt.xlabel('Zemepisná dĺžka')
plt.ylabel('Zemepisná šírka')
plt.title('Pohyb lodí 1. februára 2025')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('uloha1/pohyb_lodi.png')
plt.show()

# c) Najvyššia rýchlosť a najdlhšia prejdená trasa
# Najvyššia rýchlosť
max_speed_row = df.loc[df['Speed'].idxmax()]
print(f"Najvyššiu rýchlosť mala loď {max_speed_row['Ship_ID']} ({max_speed_row['Speed']} uzlov)")

# Najdlhšia prejdená trasa
def compute_total_distance(ship_df):
    coords = list(zip(ship_df['Latitude'], ship_df['Longitude']))
    total = 0.0
    for i in range(1, len(coords)):
        total += geodesic(coords[i-1], coords[i]).kilometers
    return total

distances = {}
for ship_id in ship_ids:
    ship_data = df[df['Ship_ID'] == ship_id]
    dist = compute_total_distance(ship_data)
    distances[ship_id] = dist

max_ship = max(distances, key=distances.get)
print(f"Najdlhšiu trasu prešla loď {max_ship} ({distances[max_ship]:.2f} km)")
