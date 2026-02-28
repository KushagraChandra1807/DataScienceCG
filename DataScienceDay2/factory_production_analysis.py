import pandas as pd
import numpy as np

production = np.array([
    [120, 150, 180, 200],
    [300, 320, 350, 400],
    [450, 480, 520, 550]
])

print("=" * 70)
print("FACTORY PRODUCTION ANALYSIS")
print("=" * 70)
print()

print("Original Production Data:")
print("Products: Gadgets, Tools, Machines")
print("Quarters: Q1, Q2, Q3, Q4")
print(production)
print()

df = pd.DataFrame(
    production,
    index=['Gadgets', 'Tools', 'Machines'],
    columns=['Q1', 'Q2', 'Q3', 'Q4']
)

print("Production Data as DataFrame:")
print(df)
print()

gadgets_series = pd.Series(production[0], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Gadgets')
tools_series = pd.Series(production[1], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Tools')
machines_series = pd.Series(production[2], index=['Q1', 'Q2', 'Q3', 'Q4'], name='Machines')

print("Gadgets Series:")
print(gadgets_series)
print()

print("Tools Series:")
print(tools_series)
print()

print("Machines Series:")
print(machines_series)
print()

production_improved = production * 1.05
print("Production after 5% efficiency improvement:")
print(production_improved)
print()

gadgets_production = production[0]
print("Gadgets production across all quarters:")
print(gadgets_production)
print()

avg_per_product = np.mean(production, axis=1)
print("Average production per product:")
print(f"Gadgets: {avg_per_product[0]:.2f}")
print(f"Tools: {avg_per_product[1]:.2f}")
print(f"Machines: {avg_per_product[2]:.2f}")
print()

exceptional_performance = production > 500
print("Exceptional performance (>500 units):")
print(exceptional_performance)
print()
print("Values exceeding 500 units:")
print(production[exceptional_performance])
