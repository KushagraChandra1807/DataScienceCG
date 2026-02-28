import numpy as np

yields = np.array([[2.5, 3.0, 1.8],
                   [2.8, 3.2, 2.0],
                   [3.1, 2.9, 2.2],
                   [2.6, 3.1, 1.9]])

print("=" * 70)
print("AGRICULTURE YIELD ANALYSIS")
print("=" * 70)
print()

print("Original crop yields (tons per hectare):")
print("         Crop A  Crop B  Crop C")
print(yields)
print()

adjustment = np.array([0.2, 0.3, 0.1])
print("Increase yields of second region (index 1) by [0.2, 0.3, 0.1]:")
print(f"Original region 1: {yields[1]}")
yields[1] = yields[1] + adjustment
print(f"Adjusted region 1: {yields[1]}")
print()
print("Updated yields:")
print("         Crop A  Crop B  Crop C")
print(yields)
print()

print("Multiply last column (Crop C) by 1.1 for fertilizer impact:")
print(f"Original Crop C yields: {yields[:, 2]}")
yields[:, 2] = yields[:, 2] * 1.1
print(f"After fertilizer Crop C: {yields[:, 2]}")
print()
print("Updated yields:")
print("         Crop A  Crop B  Crop C")
print(yields)
print()

avg_yields = np.mean(yields, axis=0)
crops = ['Crop A', 'Crop B', 'Crop C']
highest_crop_index = np.argmax(avg_yields)

print("Average yield across all regions:")
for i, crop in enumerate(crops):
    print(f"{crop}: {avg_yields[i]:.2f} tons/hectare")
print()
print(f"Highest average yield: {crops[highest_crop_index]} with {avg_yields[highest_crop_index]:.2f} tons/hectare")
