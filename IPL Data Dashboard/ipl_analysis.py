import pandas as pd

# Load Dataset
df = pd.read_csv("ipl_data.csv")

# KPI Calculations
total_matches = len(df)
total_runs = df["Runs"].sum()
total_wins = len(df[df["Result"] == "Win"])

print("🏏 IPL DATA ANALYSIS")
print("-" * 30)
print("Total Matches:", total_matches)
print("Total Runs:", total_runs)
print("Total Wins:", total_wins)

# Top Team by Runs
top_team = df.groupby("Team")["Runs"].sum().idxmax()
top_runs = df.groupby("Team")["Runs"].sum().max()

print("\nTop Team:", top_team)
print("Runs Scored:", top_runs)

# Venue with Most Matches
top_venue = df["Venue"].value_counts().idxmax()
print("Most Used Venue:", top_venue)

# Team Win Count
print("\nWin Count by Team")
print(df[df["Result"] == "Win"]["Team"].value_counts())

# Save Summary
summary = pd.DataFrame({
    "Metric": ["Total Matches", "Total Runs", "Total Wins"],
    "Value": [total_matches, total_runs, total_wins]
})

summary.to_csv("ipl_summary.csv", index=False)

print("\nSummary saved as ipl_summary.csv")