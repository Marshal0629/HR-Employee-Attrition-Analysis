import pandas as pd

# Load cleaned dataset
df = pd.read_csv("HR_Employee_Attrition_Cleaned.csv")

# Attrition distribution
attrition_counts = df["Attrition"].value_counts()

print("Attrition distribution:")
print(attrition_counts)

# Attrition rate
attrition_rate = (df["Attrition"] == "Yes").mean() * 100

print(f"\nOverall attrition rate: {attrition_rate:.2f}%")

# Attrition by overtime
overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by overtime:")
print(overtime_attrition)

# Attrition rate by Job Level
job_level_attrition = pd.crosstab(
    df["JobLevel"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Job Level:")
print(job_level_attrition)

# Attrition rate by Job Satisfaction
job_satisfaction_attrition = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Job Satisfaction:")
print(job_satisfaction_attrition)

# Employee count by Job Level
print("\nEmployee count by Job Level:")
print(df["JobLevel"].value_counts().sort_index())

# Median Monthly Income by Attrition
median_income = df.groupby("Attrition")["MonthlyIncome"].median()

print("\nMedian Monthly Income by Attrition:")
print(median_income)

import matplotlib.pyplot as plt

# Monthly Income distribution by Attrition
df.boxplot(column="MonthlyIncome", by="Attrition")

plt.title("Monthly Income Distribution by Attrition")
plt.suptitle("")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")
plt.show()

# Attrition rate by Monthly Income quartile
df["IncomeGroup"] = pd.qcut(
    df["MonthlyIncome"],
    q=4,
    labels=["Q1 - Lowest", "Q2", "Q3", "Q4 - Highest"]
)

income_group_attrition = pd.crosstab(
    df["IncomeGroup"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Monthly Income group:")
print(income_group_attrition)

# Attrition rate by Years at Company group
df["YearsAtCompanyGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, float("inf")],
    labels=["0–2 years", "3–5 years", "6–10 years", "11–20 years", "21+ years"]
)

years_at_company_attrition = pd.crosstab(
    df["YearsAtCompanyGroup"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Years at Company group:")
print(years_at_company_attrition)

print("\nEmployee count by Years at Company group:")
print(df["YearsAtCompanyGroup"].value_counts().sort_index())

# Attrition rate by Job Role
job_role_attrition = pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Job Role:")
print(job_role_attrition)

print("\nEmployee count by Job Role:")
print(df["JobRole"].value_counts())

# Attrition rate by Work Life Balance
work_life_attrition = pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Work Life Balance:")
print(work_life_attrition)

print("\nEmployee count by Work Life Balance:")
print(df["WorkLifeBalance"].value_counts().sort_index())

# Attrition rate by Environment Satisfaction
environment_attrition = pd.crosstab(
    df["EnvironmentSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Environment Satisfaction:")
print(environment_attrition)

print("\nEmployee count by Environment Satisfaction:")
print(df["EnvironmentSatisfaction"].value_counts().sort_index())

# Attrition rate by Stock Option Level
stock_option_attrition = pd.crosstab(
    df["StockOptionLevel"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Stock Option Level:")
print(stock_option_attrition)

print("\nEmployee count by Stock Option Level:")
print(df["StockOptionLevel"].value_counts().sort_index())

# Attrition rate by Business Travel
business_travel_attrition = pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Business Travel:")
print(business_travel_attrition)

print("\nEmployee count by Business Travel:")
print(df["BusinessTravel"].value_counts())

# Key HR KPIs
total_employees = len(df)
employees_left = (df["Attrition"] == "Yes").sum()
employees_stayed = (df["Attrition"] == "No").sum()
overall_attrition_rate = employees_left / total_employees * 100

median_monthly_income = df["MonthlyIncome"].median()
median_years_at_company = df["YearsAtCompany"].median()

print("\n--- Key HR KPIs ---")
print(f"Total employees: {total_employees}")
print(f"Employees who left: {employees_left}")
print(f"Employees who stayed: {employees_stayed}")
print(f"Overall attrition rate: {overall_attrition_rate:.2f}%")
print(f"Median monthly income: {median_monthly_income}")
print(f"Median years at company: {median_years_at_company}")

# Attrition by Overtime and Years at Company Group
overtime_tenure_attrition = pd.crosstab(
    [df["YearsAtCompanyGroup"], df["OverTime"]],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Years at Company and Overtime:")
print(overtime_tenure_attrition)

# Attrition by Job Role and Overtime
role_overtime_attrition = pd.crosstab(
    [df["JobRole"], df["OverTime"]],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Job Role and Overtime:")
print(role_overtime_attrition)

# Employee count by Job Role and Overtime
role_overtime_count = pd.crosstab(
    df["JobRole"],
    df["OverTime"]
)

print("\nEmployee count by Job Role and Overtime:")
print(role_overtime_count)

# Attrition by Income Group and Overtime
income_overtime_attrition = pd.crosstab(
    [df["IncomeGroup"], df["OverTime"]],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Income Group and Overtime:")
print(income_overtime_attrition)

# Employee count by Income Group and Overtime
income_overtime_count = pd.crosstab(
    df["IncomeGroup"],
    df["OverTime"]
)

print("\nEmployee count by Income Group and Overtime:")
print(income_overtime_count)

# Attrition by Job Role and Income Group
role_income_attrition = pd.crosstab(
    [df["JobRole"], df["IncomeGroup"]],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by Job Role and Income Group:")
print(role_income_attrition)

# Employee count by Job Role and Income Group
role_income_count = pd.crosstab(
    df["JobRole"],
    df["IncomeGroup"]
)

print("\nEmployee count by Job Role and Income Group:")
print(role_income_count)

