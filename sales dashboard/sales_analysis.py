import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Sales"] = pd.to_numeric(df["Sales"])
df["Profit"] = pd.to_numeric(df["Profit"])

print("Revenue:", df["Sales"].sum())
print("Profit:", df["Profit"].sum())

top_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Top Selling Product:", top_product)