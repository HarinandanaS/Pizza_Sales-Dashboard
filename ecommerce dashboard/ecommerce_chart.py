import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_data.csv")

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("ecommerce_chart.png")

plt.show()