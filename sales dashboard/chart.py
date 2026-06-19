import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

sales_by_product = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(6,4))
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("sales_chart.png")