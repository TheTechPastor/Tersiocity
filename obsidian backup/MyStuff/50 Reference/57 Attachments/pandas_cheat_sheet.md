# 🐼 Pandas Cheat Sheet

## 📦 Setup
```python
import pandas as pd
```

## 📁 Read / Write Files
```python
# Read
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")

# Write
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")
```

## 📊 Create a DataFrame
```python
data = {
    "Name": ["Alice", "Bob"],
    "Hours": [5, 8]
}
df = pd.DataFrame(data)
```

## 🔍 View / Inspect
```python
df.head()         # First 5 rows
df.tail(3)        # Last 3 rows
df.info()         # Schema and non-null counts
df.describe()     # Stats for numeric columns
df.columns        # Column names
df.shape          # (rows, columns)
```

## 🔎 Select / Filter
```python
df["Hours"]             # Select a column (Series)
df[["Name", "Hours"]]   # Multiple columns
df.loc[0]               # Row by index label
df.iloc[0]              # Row by position

# Filter rows
df[df["Hours"] > 6]
```

## 🔄 Modify Columns
```python
df["Hours2"] = df["Hours"] * 2
df.rename(columns={"Hours": "TotalHours"}, inplace=True)
df.drop(columns=["TempCol"], inplace=True)
```

## 🧹 Clean Data
```python
df.dropna()                      # Drop rows with nulls
df.fillna(0)                     # Replace nulls with 0
df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime
df["Hours"] = df["Hours"].astype(float)  # Change type
```

## 🧮 Group & Aggregate
```python
df.groupby("Name")["Hours"].sum()
df.groupby("UserID").agg({"Hours": "mean", "Project": "count"})
```

## 🔗 Merge / Join
```python
pd.merge(df1, df2, on="UserID", how="left")  # like SQL left join
```

## 📆 Time Series
```python
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
df.resample("W").sum()    # Weekly
df.resample("M").mean()   # Monthly
```

## 🗂 Sort / Unique / Duplicates
```python
df.sort_values(by="Hours", ascending=False)
df["Name"].unique()
df.duplicated().sum()
df.drop_duplicates(inplace=True)
```

## 📤 Export Summary Reports
```python
summary = df.groupby("UserID")["Hours"].sum().reset_index()
summary.to_excel("summary_report.xlsx", index=False)
```

## 🧰 Handy Snippets
| Task                          | Code                                       |
|-------------------------------|--------------------------------------------|
| Check for nulls              | `df.isnull().sum()`                        |
| Conditional column           | `df["Overtime"] = df["Hours"] > 8`        |
| Count rows per value         | `df["Name"].value_counts()`               |
| Get top N entries            | `df.nlargest(5, "Hours")`                 |
