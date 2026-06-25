import pandas as pd

df = pd.read_csv("pizza_data.csv")

print("🍕 Pizza Sales Dashboard")
print("-" * 30)

print("Total Orders:", len(df))
print("Total Revenue:", df["Revenue"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Best Selling Pizza:", df.groupby("Pizza")["Quantity"].sum().idxmax())
print("Top Category:", df.groupby("Category")["Revenue"].sum().idxmax())