import pandas as pd

# Load cleaned dataset
df = pd.read_csv("HR_Employee_Attrition_Cleaned.csv")

# Create Monthly Income groups
df["IncomeGroup"] = pd.qcut(
    df["MonthlyIncome"],
    q=4,
    labels=["Q1 - Lowest", "Q2", "Q3", "Q4 - Highest"]
)

# Create Years at Company groups
df["YearsAtCompanyGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, float("inf")],
    labels=["0–2 years", "3–5 years", "6–10 years", "11–20 years", "21+ years"]
)

# Save Tableau-ready dataset
df.to_csv("HR_Employee_Attrition_Tableau.csv", index=False)

print("Tableau-ready dataset created successfully.")
print(f"Shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
