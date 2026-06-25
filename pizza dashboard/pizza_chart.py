import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pizza_data.csv")

sales = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(6,4))
sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("pizza_chart.png")
plt.show()