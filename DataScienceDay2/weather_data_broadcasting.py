import numpy as np

temps = np.array([[25, 28, 30],
                  [22, 24, 26],
                  [30, 32, 33],
                  [27, 29, 31],
                  [20, 21, 23]])

print("=" * 70)
print("WEATHER DATA BROADCASTING")
print("=" * 70)
print()

print("Original temperatures (Celsius):")
print(temps)
print(f"Shape: {temps.shape} (5 cities × 3 days)")
print()

temps_fahrenheit = temps * 9/5 + 32
print("Temperatures converted to Fahrenheit:")
print(temps_fahrenheit)
print()

correction_factor = np.array([1, -1, 0])
print("Correction factor:", correction_factor)
print("Shape:", correction_factor.shape)
print()

temps_corrected = temps + correction_factor
print("Corrected temperatures (Celsius):")
print(temps_corrected)
print()

print("Broadcasting explanation:")
print("- Original temps shape: (5, 3) - 5 cities, 3 days")
print("- Correction factor shape: (3,) - 3 values for 3 days")
print("- NumPy broadcasts the correction factor across all 5 cities")
print("- Day 1: +1°C, Day 2: -1°C, Day 3: +0°C for all cities")
print("- Result shape: (5, 3) - same as original")
