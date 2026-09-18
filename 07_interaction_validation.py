import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from statsmodels.stats.multitest import multipletests

# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("HR_Employee_Attrition_Cleaned.csv")

# Create income groups
df["IncomeGroup"] = pd.qcut(
    df["MonthlyIncome"],
    q=4,
    labels=[
        "Q1 - Lowest",
        "Q2",
        "Q3",
        "Q4 - Highest"
    ]
)

# Create tenure groups
df["YearsAtCompanyGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, float("inf")],
    labels=[
        "0–2 years",
        "3–5 years",
        "6–10 years",
        "11–20 years",
        "21+ years"
    ]
)

# =========================================================
# 2. CREATE INTERACTION VARIABLES
# =========================================================

df["Tenure_Overtime"] = (
    df["YearsAtCompanyGroup"].astype(str)
    + " + "
    + df["OverTime"]
)

df["Income_Overtime"] = (
    df["IncomeGroup"].astype(str)
    + " + "
    + df["OverTime"]
)

df["Role_Overtime"] = (
    df["JobRole"].astype(str)
    + " + "
    + df["OverTime"]
)

# =========================================================
# 3. FUNCTION FOR CHI-SQUARE TEST
# =========================================================

def interaction_test(variable):

    table = pd.crosstab(
        df[variable],
        df["Attrition"]
    )

    chi2, p_value, dof, expected = chi2_contingency(
        table
    )

    n = table.values.sum()

    min_dimension = min(
        table.shape[0] - 1,
        table.shape[1] - 1
    )

    cramers_v = np.sqrt(
        chi2 / (n * min_dimension)
    )

    return p_value, cramers_v


# =========================================================
# 4. TEST INTERACTIONS
# =========================================================

interaction_variables = [
    "Tenure_Overtime",
    "Income_Overtime",
    "Role_Overtime"
]

results = []

for variable in interaction_variables:

    p_value, effect_size = interaction_test(variable)

    results.append({
        "Interaction": variable,
        "P_Value": p_value,
        "Effect_Size": effect_size
    })

results = pd.DataFrame(results)

# =========================================================
# 5. MULTIPLE TESTING CORRECTION
# =========================================================

reject, adjusted_p, _, _ = multipletests(
    results["P_Value"],
    method="fdr_bh"
)

results["Adjusted_P_Value"] = adjusted_p
results["Significant"] = reject

# =========================================================
# 6. DISPLAY
# =========================================================

print("\n" + "=" * 70)
print("INTERACTION STATISTICAL VALIDATION")
print("=" * 70)

print(
    results.to_string(index=False)
)

# =========================================================
# 7. DISPLAY SEGMENT ATTRITION RATES
# =========================================================

print("\n" + "=" * 70)
print("KEY HIGH-RISK SEGMENTS")
print("=" * 70)

for variable in interaction_variables:

    print(f"\n--- {variable} ---")

    table = pd.crosstab(
        df[variable],
        df["Attrition"],
        normalize="index"
    ) * 100

    print(table.round(2))

# =========================================================
# 8. SAVE RESULTS
# =========================================================

results.to_csv(
    "Interaction_Validation_Results.csv",
    index=False
)

print(
    "\nResults saved to:"
    "\nInteraction_Validation_Results.csv"
)
