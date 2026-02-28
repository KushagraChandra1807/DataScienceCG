import pandas as pd
import numpy as np

df = pd.read_csv('retail/sample_data1 - Sheet1.csv')

print("=" * 70)
print("ORIGINAL DATAFRAME")
print("=" * 70)
print(df)
print()

print("=" * 70)
print("SINGLE CONDITION FILTERING")
print("=" * 70)

high_salary = df[df['Salary'] > 50000]
print("\nEmployees with Salary > 50000:")
print(high_salary[['Employee_ID', 'Department', 'Salary', 'Region']])
print()

sales_dept = df[df['Department'] == 'Sales']
print("Sales Department Employees:")
print(sales_dept[['Employee_ID', 'Department', 'Salary', 'Monthly_Sales']])
print()

print("=" * 70)
print("MULTIPLE CONDITIONS (AND)")
print("=" * 70)

condition1 = df[(df['Salary'] > 45000) & (df['Performance_Rating'] >= 4)]
print("\nSalary > 45000 AND Performance Rating >= 4:")
print(condition1[['Employee_ID', 'Department', 'Salary', 'Performance_Rating']])
print()

condition2 = df[(df['Department'] == 'Sales') & (df['Monthly_Sales'] > 130000)]
print("Department = Sales AND Monthly Sales > 130000:")
print(condition2[['Employee_ID', 'Department', 'Salary', 'Monthly_Sales']])
print()

condition3 = df[(df['Region'] == 'North') & (df['Experience_Years'] >= 3)]
print("Region = North AND Experience >= 3 years:")
print(condition3[['Employee_ID', 'Department', 'Region', 'Experience_Years', 'Salary']])
print()

print("=" * 70)
print("MULTIPLE CONDITIONS (OR)")
print("=" * 70)

condition4 = df[(df['Department'] == 'Sales') | (df['Department'] == 'IT')]
print("\nDepartment = Sales OR IT:")
print(condition4[['Employee_ID', 'Department', 'Salary', 'Experience_Years']])
print()

condition5 = df[(df['Salary'] > 55000) | (df['Performance_Rating'] == 5)]
print("Salary > 55000 OR Performance Rating = 5:")
print(condition5[['Employee_ID', 'Department', 'Salary', 'Performance_Rating']])
print()

print("=" * 70)
print("COMPLEX CONDITIONS (AND + OR)")
print("=" * 70)

condition6 = df[((df['Department'] == 'Sales') | (df['Department'] == 'Marketing')) & (df['Salary'] > 48000)]
print("\n(Sales OR Marketing) AND Salary > 48000:")
print(condition6[['Employee_ID', 'Department', 'Salary', 'Region']])
print()

condition7 = df[(df['Region'] == 'North') & ((df['Performance_Rating'] >= 4) | (df['Experience_Years'] >= 5))]
print("Region = North AND (Performance >= 4 OR Experience >= 5):")
print(condition7[['Employee_ID', 'Region', 'Performance_Rating', 'Experience_Years', 'Salary']])
print()

print("=" * 70)
print("SORTING - SINGLE COLUMN")
print("=" * 70)

sorted_asc = df.sort_values('Salary', ascending=True)
print("\nSorted by Salary (Ascending):")
print(sorted_asc[['Employee_ID', 'Department', 'Salary']])
print()

sorted_desc = df.sort_values('Salary', ascending=False)
print("Sorted by Salary (Descending):")
print(sorted_desc[['Employee_ID', 'Department', 'Salary']])
print()

print("=" * 70)
print("SORTING - MULTIPLE COLUMNS")
print("=" * 70)

sorted_multi = df.sort_values(['Department', 'Salary'], ascending=[True, False])
print("\nSorted by Department (Asc) then Salary (Desc):")
print(sorted_multi[['Employee_ID', 'Department', 'Salary', 'Region']])
print()

sorted_multi2 = df.sort_values(['Region', 'Experience_Years'], ascending=[True, False])
print("Sorted by Region (Asc) then Experience (Desc):")
print(sorted_multi2[['Employee_ID', 'Region', 'Experience_Years', 'Salary']])
print()

print("=" * 70)
print("SERIES OPERATIONS WITH CONDITIONS")
print("=" * 70)

salary_series = df['Salary']
print("\nOriginal Salary Series:")
print(salary_series)
print()

high_salary_series = salary_series[salary_series > 50000]
print("Salary > 50000 (Series):")
print(high_salary_series)
print()

sorted_series = salary_series.sort_values(ascending=False)
print("Sorted Salary Series (Descending):")
print(sorted_series)
print()

performance_series = df['Performance_Rating']
print("Performance Rating Series:")
print(performance_series)
print()

high_performers = performance_series[performance_series >= 4]
print("High Performers (Rating >= 4):")
print(high_performers)
print()

print("=" * 70)
print("DATAFRAME WITH SORTING AND CONDITIONS COMBINED")
print("=" * 70)

filtered_sorted = df[df['Salary'] > 45000].sort_values('Salary', ascending=False)
print("\nFiltered (Salary > 45000) and Sorted (Descending):")
print(filtered_sorted[['Employee_ID', 'Department', 'Salary', 'Experience_Years']])
print()

complex_query = df[(df['Region'] == 'North') | (df['Region'] == 'South')].sort_values(['Region', 'Salary'], ascending=[True, False])
print("Region = North OR South, sorted by Region and Salary:")
print(complex_query[['Employee_ID', 'Region', 'Department', 'Salary']])
print()

sales_sorted = df[df['Department'] == 'Sales'].sort_values('Monthly_Sales', ascending=False)
print("Sales Department sorted by Monthly Sales (Descending):")
print(sales_sorted[['Employee_ID', 'Department', 'Monthly_Sales', 'Salary']])


print("=" * 70)
print("GROUP BY OPERATIONS")
print("=" * 70)

print("\nGroup by Region - Monthly Sales Sum:")
region_sales = df.groupby('Region')['Monthly_Sales'].sum()
print(region_sales)
print()

print("Group by Region - Monthly Sales Mean:")
region_sales_mean = df.groupby('Region')['Monthly_Sales'].mean()
print(region_sales_mean)
print()

print("Group by Region - Monthly Sales Count:")
region_sales_count = df.groupby('Region')['Monthly_Sales'].count()
print(region_sales_count)
print()

print("Group by Region - Multiple Aggregations on Monthly Sales:")
region_sales_agg = df.groupby('Region')['Monthly_Sales'].agg(['sum', 'mean', 'count', 'max', 'min'])
print(region_sales_agg)
print()

print("Group by Department and Region - Monthly Sales Sum:")
dept_region_sales = df.groupby(['Department', 'Region'])['Monthly_Sales'].sum()
print(dept_region_sales)
print()

print("Group by Region - Salary and Monthly Sales:")
region_multi = df.groupby('Region')[['Salary', 'Monthly_Sales']].sum()
print(region_multi)
print()

print("Group by Department - Monthly Sales Sum:")
dept_sales = df.groupby('Department')['Monthly_Sales'].sum()
print(dept_sales)
print()

print("Group by Department - Average Salary:")
dept_salary = df.groupby('Department')['Salary'].mean()
print(dept_salary)
