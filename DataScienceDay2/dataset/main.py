import pandas as pd

df = pd.read_csv("telecom_churn - Sheet1.csv")

print("=" * 70)
print("TELECOM CHURN DATASET ANALYSIS")
print("=" * 70)
print()

print("Total number of records:")
print(df.shape[0])
print()

print("Missing values in each column:")
print(df.isnull().sum())
print()

print("Average Monthly Charges:")
print(df["Monthly_Charges"].mean())
print()

print("Contract Type distribution:")
print(df["Contract_Type"].value_counts())
print()

print("Churn distribution:")
print(df["Churn"].value_counts())
print()

print("Crosstab - Contract Type vs Churn:")
print(pd.crosstab(df["Contract_Type"], df["Churn"]))
print()

total = df.shape[0]
avg = df["Monthly_Charges"].mean()
max_contract = df["Contract_Type"].value_counts().idxmax()

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Total Records: {total}")
print(f"Average Monthly Charges: {avg:.2f}")
print(f"Most Common Contract Type: {max_contract}")