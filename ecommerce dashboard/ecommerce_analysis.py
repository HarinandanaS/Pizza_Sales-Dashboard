import pandas as pd

df = pd.read_csv("ecommerce_data.csv")

print("Total Revenue:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

top_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Top Product:", top_product)

top_category = df.groupby("Category")["Sales"].sum().idxmax()
print("Top Category:", top_category)

top_region = df.groupby("Region")["Sales"].sum().idxmax()
print("Top Region:", top_region)