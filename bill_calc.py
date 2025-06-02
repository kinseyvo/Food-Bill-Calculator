import pandas as pd

# Sample data (replace as needed)
data = {
    "Person": ["Alice", "Alice", "Alice", "Bob", "Carol"],
    "Food": ["Cheeseburger", "Fries", "Soda", "Pasta", "Salad"],
    "Food Price": [12.00, 5.00, 3.00, 14.00, 10.00]
}

df = pd.DataFrame(data)

# Tax and tip rates (replace as needed)
tax_rate = 0.0875
tip_rate = 0.18

# Formulas for Excel
df["Tax"] = [f"=C{i+2}*{tax_rate}" for i in range(len(df))]
df["Tip"] = [f"=C{i+2}*{tip_rate}" for i in range(len(df))]
df["Total"] = [f"=C{i+2}+D{i+2}+E{i+2}" for i in range(len(df))]

columns = ["Person", "Food", "Food Price", "Tax", "Tip", "Total"]
df = df[columns]

# Summary rows for each person
summary_rows = [
    ["Alice", "", "", "", "", "=SUMIFS(F:F,A:A,\"Alice\")"],
    ["Bob", "", "", "", "", "=SUMIFS(F:F,A:A,\"Bob\")"],
    ["Carol", "", "", "", "", "=SUMIFS(F:F,A:A,\"Carol\")"]
]

summary_df = pd.DataFrame(summary_rows, columns=columns)

# Combine data and summary
final_df = pd.concat([df, summary_df], ignore_index=True)

# Save to Excel
file_path = "/Downloads/Restaurant_Bill_Tracker.xlsx"
final_df.to_excel(file_path, index=False)

file_path
