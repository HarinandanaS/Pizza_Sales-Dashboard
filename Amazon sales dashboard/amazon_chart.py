import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("amazon_data.csv")

# Group data by Category and calculate total Sales
sales = df.groupby("Category")["Sales"].sum()

# Create bar chart
plt.figure(figsize=(8,5))
sales.plot(kind="bar")

# Chart title and labels
plt.title("Amazon Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Save chart
plt.tight_layout()
plt.savefig("amazon_sales_chart.png")

# Display chart
plt.show()