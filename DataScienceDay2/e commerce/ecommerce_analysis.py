import pandas as pd
import numpy as np

print("=" * 80)
print("E-COMMERCE DATA WRANGLING PROJECT")
print("=" * 80)
print()

# ============================================================================
# TASK 1: DATA LOADING
# ============================================================================
print("TASK 1: DATA LOADING")
print("-" * 80)

customers_df = pd.read_csv('Customers1 - Sheet1.csv')
sales_df = pd.read_csv('Sales1 - Sheet1.csv')
support_df = pd.read_csv('support1 - Sheet1.csv')

print("\nCustomers Dataset:")
print(f"Shape: {customers_df.shape}")
print(f"Columns: {list(customers_df.columns)}")
print(customers_df)
print(f"\nMissing Values:\n{customers_df.isnull().sum()}")
print()

print("Sales Dataset:")
print(f"Shape: {sales_df.shape}")
print(f"Columns: {list(sales_df.columns)}")
print(sales_df)
print(f"\nMissing Values:\n{sales_df.isnull().sum()}")
print()

print("Support Dataset:")
print(f"Shape: {support_df.shape}")
print(f"Columns: {list(support_df.columns)}")
print(support_df)
print(f"\nMissing Values:\n{support_df.isnull().sum()}")
print()

# ============================================================================
# TASK 2: ARRAY OPERATIONS & BROADCASTING
# ============================================================================
print("=" * 80)
print("TASK 2: ARRAY OPERATIONS & BROADCASTING")
print("-" * 80)

# Create NumPy array of prices
prices_array = sales_df['Price'].values
print("\nOriginal Prices (NumPy Array):")
print(prices_array)
print()

# Apply 10% discount using broadcasting
discount_rate = 0.10
discounted_prices = prices_array * (1 - discount_rate)
print("Discounted Prices (10% off using Broadcasting):")
print(discounted_prices)
print()

# Compute total revenue per order
sales_df['Revenue'] = sales_df['Quantity'] * sales_df['Price']
print("Revenue per Order (Quantity × Price):")
print(sales_df[['OrderID', 'Quantity', 'Price', 'Revenue']])
print()

# ============================================================================
# TASK 3: INDEXING & SLICING
# ============================================================================
print("=" * 80)
print("TASK 3: INDEXING & SLICING")
print("-" * 80)

# Convert OrderDate to datetime
sales_df['OrderDate'] = pd.to_datetime(sales_df['OrderDate'])

# Extract orders from January 2025
january_2025_orders = sales_df[(sales_df['OrderDate'].dt.month == 1) & (sales_df['OrderDate'].dt.year == 2025)]
print("\nOrders placed in January 2025:")
if len(january_2025_orders) > 0:
    print(january_2025_orders)
else:
    print("No orders found in January 2025 (sample data is from 2023)")
print()

# Slice first 10 rows
print("First 10 rows of Sales Dataset:")
print(sales_df.head(10))
print()

# ============================================================================
# TASK 4: FILTERING
# ============================================================================
print("=" * 80)
print("TASK 4: FILTERING")
print("-" * 80)

# Filter customers from North region
north_customers = customers_df[customers_df['Region'] == 'North']
print("\nCustomers from North Region:")
print(north_customers)
print()

# Identify orders with revenue > ₹10,000
high_revenue_orders = sales_df[sales_df['Revenue'] > 10000]
print("Orders with Revenue > ₹10,000:")
print(high_revenue_orders[['OrderID', 'CustomerID', 'Product', 'Revenue']])
print()

# ============================================================================
# TASK 5: SORTING
# ============================================================================
print("=" * 80)
print("TASK 5: SORTING")
print("-" * 80)

# Convert SignupDate to datetime
customers_df['SignupDate'] = pd.to_datetime(customers_df['SignupDate'])

# Sort customers by Signup Date (oldest to newest)
customers_sorted = customers_df.sort_values('SignupDate', ascending=True)
print("\nCustomers sorted by Signup Date (Oldest to Newest):")
print(customers_sorted[['CustomerID', 'Name', 'SignupDate']])
print()

# Sort sales by Revenue (descending)
sales_sorted = sales_df.sort_values('Revenue', ascending=False)
print("Sales sorted by Revenue (Highest to Lowest):")
print(sales_sorted[['OrderID', 'CustomerID', 'Product', 'Revenue']])
print()

# ============================================================================
# TASK 6: GROUPING
# ============================================================================
print("=" * 80)
print("TASK 6: GROUPING")
print("-" * 80)

# Merge sales with customers to get Region info
sales_with_region = sales_df.merge(customers_df[['CustomerID', 'Region']], on='CustomerID', how='left')

# Group sales by Region and calculate average revenue
print("\nGroup by Region - Average Revenue:")
avg_revenue_by_region = sales_with_region.groupby('Region')['Revenue'].mean()
print(avg_revenue_by_region)
print()

# Group support tickets by Issue Type and find average resolution time
print("Group by Issue Type - Average Resolution Time (hours):")
avg_resolution_by_issue = support_df.groupby('IssueType')['ResolutionTime'].mean()
print(avg_resolution_by_issue)
print()

# ============================================================================
# TASK 7: DATA WRANGLING
# ============================================================================
print("=" * 80)
print("TASK 7: DATA WRANGLING")
print("-" * 80)

# Handle missing values - fill missing ages with median age
median_age = customers_df['Age'].median()
customers_df['Age'] = customers_df['Age'].fillna(median_age)
print(f"\nMissing ages filled with median age: {median_age}")
print("Updated Customers Dataset:")
print(customers_df)
print()

# Rename columns for clarity
support_df = support_df.rename(columns={
    'TicketID': 'Ticket_ID',
    'IssueType': 'Issue_Type',
    'ResolutionTime': 'Resolution_Time'
})
print("Support Dataset with renamed columns:")
print(support_df)
print()

# Merge all datasets on CustomerID
merged_df = customers_df.merge(sales_df, on='CustomerID', how='left')
merged_df = merged_df.merge(support_df, on='CustomerID', how='left')
print(f"Merged Dataset Shape: {merged_df.shape}")
print("Merged Dataset Preview:")
print(merged_df.head())
print()

# Create calculated fields
# Customer Lifetime Value (CLV) = total revenue per customer
clv = sales_df.groupby('CustomerID')['Revenue'].sum().reset_index()
clv = clv.rename(columns={'Revenue': 'CLV'})

# Average Resolution Time per Customer
avg_resolution_per_customer = support_df.groupby('CustomerID')['Resolution_Time'].mean().reset_index()
avg_resolution_per_customer = avg_resolution_per_customer.rename(columns={'Resolution_Time': 'Avg_Resolution_Time'})

# Create final cleaned dataset
final_df = customers_df.merge(clv, on='CustomerID', how='left')
final_df = final_df.merge(avg_resolution_per_customer, on='CustomerID', how='left')

# Fill NaN values
final_df['CLV'] = final_df['CLV'].fillna(0)
final_df['Avg_Resolution_Time'] = final_df['Avg_Resolution_Time'].fillna(0)

print("Final Cleaned Dataset with Calculated Fields:")
print(final_df)
print()

# Export to CSV
final_df.to_csv('Cleaned_Data.csv', index=False)
print("✓ Cleaned dataset exported to 'Cleaned_Data.csv'")
print()

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================
print("=" * 80)
print("SUMMARY STATISTICS FOR ML/DL MODEL")
print("-" * 80)

print(f"\nTotal Customers: {len(customers_df)}")
print(f"Total Orders: {len(sales_df)}")
print(f"Total Support Tickets: {len(support_df)}")
print(f"Total Revenue: ₹{sales_df['Revenue'].sum():,.2f}")
print(f"Average Order Value: ₹{sales_df['Revenue'].mean():,.2f}")
print(f"Average Customer Lifetime Value: ₹{final_df['CLV'].mean():,.2f}")
print(f"Average Resolution Time: {support_df['Resolution_Time'].mean():.2f} hours")
print()

print("=" * 80)
print("DATA WRANGLING COMPLETED SUCCESSFULLY!")
print("Dataset is ready for ML/DL model training")
print("=" * 80)
