import pandas as pd
from geopy.distance import geodesic

# Načítanie dát
path = 'uloha1/pohyby_lodi.xlsx'
df = pd.read_excel(path)
ship_ids = df['Ship_ID'].unique()

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