import numpy as np

crop_yields = np.array([
    [2800, 3200, 2900, 2600],
    [3100, 3400, 3000, 2800],
    [2700, 3300, 3100, 2500]
])

print("=" * 70)
print("FARM CROP YIELD ANALYSIS")
print("=" * 70)
print()

print("Original Crop Yields (kg):")
print("Crops: Wheat, Rice, Corn")
print("Seasons: Spring, Summer, Autumn, Winter")
print(crop_yields)
print()

improved_yields = crop_yields * 1.10
print("Improved Yields (10% increase):")
print(improved_yields)
print()

wheat_yields = crop_yields[0]
print("Wheat Yields Across Seasons:")
print(wheat_yields)
print()

average_per_crop = np.mean(crop_yields, axis=1)
print("Average Yield Per Crop (across all seasons):")
print(f"Wheat: {average_per_crop[0]:.2f} kg")
print(f"Rice: {average_per_crop[1]:.2f} kg")
print(f"Corn: {average_per_crop[2]:.2f} kg")
print()

high_yields = crop_yields > 3000
print("Yields Greater Than 3000 kg (Boolean mask):")
print(high_yields)
print()

print("Specific High-Performing Yields:")
print(crop_yields[high_yields])
