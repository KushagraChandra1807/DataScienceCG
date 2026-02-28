import numpy as np

sales_day1 = np.array([120, 85, 60])
sales_day2 = np.array([150, 90, 75])

print("=" * 70)
print("RETAIL SALES ANALYSIS")
print("=" * 70)
print()

total_sales = sales_day1 + sales_day2
print("Total sales per product (A, B, C):")
print(f"Product A: {total_sales[0]}")
print(f"Product B: {total_sales[1]}")
print(f"Product C: {total_sales[2]}")
print(f"Array: {total_sales}")
print()

percentage_growth = ((sales_day2 - sales_day1) / sales_day1) * 100
print("Percentage growth from day 1 to day 2:")
print(f"Product A: {percentage_growth[0]:.2f}%")
print(f"Product B: {percentage_growth[1]:.2f}%")
print(f"Product C: {percentage_growth[2]:.2f}%")
print(f"Array: {percentage_growth}")
print()

highest_growth_index = np.argmax(percentage_growth)
products = ['A', 'B', 'C']
print("Product with highest growth:")
print(f"Product {products[highest_growth_index]} with {percentage_growth[highest_growth_index]:.2f}% growth")
