import pandas as pd

hr = pd.read_csv("employee_attrition - Sheet1.csv")
attrition_rate = hr.groupby("Department")["Attrition"].value_counts(normalize=True).unstack()
print("Attrition Rate by Department")
print(attrition_rate)

sales = pd.read_csv("Sales1 - Sheet1.csv")
sales_columns = sales.columns

if "Region" in sales_columns and "Product" in sales_columns and "Sales" in sales_columns:
    sales_summary = sales.groupby(["Region", "Product"])["Sales"].sum().reset_index()
else:
    sales_summary = sales.groupby([sales_columns[0], sales_columns[1]])[sales_columns[-1]].sum().reset_index()

missing_data = sales.isnull().sum()
print("Sales Summary")
print(sales_summary)
print("Missing Data")
print(missing_data)

telecom = pd.read_csv("telecom_churn - Sheet1.csv")
churn_rate = telecom["Churn"].value_counts(normalize=True)
churn_factors = telecom.groupby("Churn").mean(numeric_only=True)

print("Churn Rate")
print(churn_rate)
print("Churn Factors")
print(churn_factors)
