import numpy as np

bp = np.array([[120, 80],
               [135, 85],
               [140, 90],
               [110, 70],
               [125, 75]])

print("=" * 70)
print("HEALTHCARE DATASET INDEXING")
print("=" * 70)
print()

print("Original blood pressure readings [systolic, diastolic]:")
print(bp)
print()

systolic = bp[:, 0]
print("Systolic values (first column):")
print(f"{systolic}")
print()

high_systolic_mask = systolic > 130
high_systolic_patients = np.where(high_systolic_mask)[0]
print("Patients with systolic > 130:")
print(f"Boolean mask: {high_systolic_mask}")
print(f"Patient indices: {high_systolic_patients}")
print("Patient readings:")
for idx in high_systolic_patients:
    print(f"   Patient {idx}: {bp[idx]}")
print()

bp_corrected = bp.copy()
diastolic_mask = bp_corrected[:, 1] < 80
bp_corrected[diastolic_mask, 1] = 80

print("Replace diastolic values < 80 with 80:")
print(f"Diastolic values < 80 mask: {diastolic_mask}")
print("Corrected blood pressure readings:")
print(bp_corrected)
print()
print("Changes made:")
for idx in np.where(diastolic_mask)[0]:
    print(f"   Patient {idx}: {bp[idx]} → {bp_corrected[idx]}")
