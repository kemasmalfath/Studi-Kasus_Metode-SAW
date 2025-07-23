import numpy as np

# Data
data = {
    "Andi": {"cash": 100, "asset": 500, "age": 35},
    "Budi ": {"cash": 200, "asset": 300, "age": 40},
    "Cici": {"cash": 150, "asset": 700, "age": 28},
    "Dedi": {"cash": 50, "asset": 200, "age": 45}
}

# Bobot
weights = {"cash": 0.3, "asset": 0.4, "age": 0.3}

# Normalisasi
max_cash = max([v["cash"] for v in data.values()])
max_asset = max([v["asset"] for v in data.values()])
min_age = min([v["age"] for v in data.values()])

for name in data:
    # Benefit: Cash dan Asset
    data[name]["norm_cash"] = data[name]["cash"] / max_cash
    data[name]["norm_asset"] = data[name]["asset"] / max_asset
    # Cost: Usia
    data[name]["norm_age"] = min_age / data[name]["age"]

# Hitung Nilai V
for name in data:
    data[name]["V"] = (weights["cash"] * data[name]["norm_cash"]) + \
                      (weights["asset"] * data[name]["norm_asset"]) + \
                      (weights["age"] * data[name]["norm_age"])

# Ranking
ranking = sorted(data.items(), key=lambda x: x[1]["V"], reverse=True)

# Output
print("===== HASIL PERHITUNGAN SAW =====")
for i, (name, attr) in enumerate(ranking, start=1):
    print(f"{i}. {name}: V = {attr['V']:.3f}")
