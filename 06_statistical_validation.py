import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, mannwhitneyu
from statsmodels.stats.multitest import multipletests

# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("HR_Employee_Attrition_Cleaned.csv")

print("Dataset shape:", df.shape)

# =========================================================
# 2. CATEGORICAL VARIABLES
# =========================================================

categorical_columns = [
    "BusinessTravel",
    "Department",
    "Education",
    "EducationField",
    "EnvironmentSatisfaction",
    "Gender",
    "JobInvolvement",
    "JobLevel",
    "JobRole",
    "JobSatisfaction",
    "MaritalStatus",
    "OverTime",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "WorkLifeBalance"
]

# =========================================================
# 3. CHI-SQUARE + CRAMER'S V
# =========================================================

categorical_results = []

for column in categorical_columns:

    table = pd.crosstab(
        df[column],
        df["Attrition"]
    )

    chi2, p_value, dof, expected = chi2_contingency(table)

    n = table.values.sum()

    min_dimension = min(
        table.shape[0] - 1,
        table.shape[1] - 1
    )

    cramers_v = np.sqrt(
        chi2 / (n * min_dimension)
    )

    categorical_results.append({
        "Variable": column,
        "Test": "Chi-square",
        "P_Value": p_value,
        "Effect_Size": cramers_v
    })

categorical_results = pd.DataFrame(categorical_results)

# =========================================================
# 4. NUMERICAL VARIABLES
# =========================================================

continuous_columns = [
    "Age",
    "DailyRate",
    "DistanceFromHome",
    "HourlyRate",
    "MonthlyIncome",
    "MonthlyRate",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

# =========================================================
# 5. MANN-WHITNEY U + EFFECT SIZE
# =========================================================

numerical_results = []

for column in continuous_columns:

    stayed = df.loc[
        df["Attrition"] == "No",
        column
    ]

    left = df.loc[
        df["Attrition"] == "Yes",
        column
    ]

    statistic, p_value = mannwhitneyu(
        stayed,
        left,
        alternative="two-sided"
    )

    n1 = len(stayed)
    n2 = len(left)

    rank_biserial = (
        2 * statistic / (n1 * n2)
    ) - 1

    numerical_results.append({
        "Variable": column,
        "Test": "Mann-Whitney U",
        "P_Value": p_value,
        "Effect_Size": abs(rank_biserial)
    })

numerical_results = pd.DataFrame(numerical_results)

# =========================================================
# 6. COMBINE RESULTS
# =========================================================

results = pd.concat(
    [categorical_results, numerical_results],
    ignore_index=True
)

# =========================================================
# 7. FDR MULTIPLE-TESTING CORRECTION
# =========================================================

reject, adjusted_p_values, _, _ = multipletests(
    results["P_Value"],
    method="fdr_bh"
)

results["Adjusted_P_Value"] = adjusted_p_values
results["Significant"] = reject

# =========================================================
# 8. EFFECT SIZE INTERPRETATION
# =========================================================

def interpret_effect_size(value):

    if value < 0.10:
        return "Very small"

    elif value < 0.20:
        return "Small"

    elif value < 0.30:
        return "Moderate"

    else:
        return "Large"


results["Effect_Strength"] = results["Effect_Size"].apply(
    interpret_effect_size
)

# =========================================================
# 9. SORT RESULTS
# =========================================================

results = results.sort_values(
    "Adjusted_P_Value"
).reset_index(drop=True)

# =========================================================
# 10. FORMAT P-VALUES FOR DISPLAY
# =========================================================

def format_p_value(value):

    if value < 0.001:
        return "< 0.001"

    return f"{value:.4f}"


results["P_Value_Display"] = results["P_Value"].apply(
    format_p_value
)

results["Adjusted_P_Value_Display"] = (
    results["Adjusted_P_Value"].apply(format_p_value)
)

# =========================================================
# 11. DISPLAY RESULTS
# =========================================================

pd.set_option("display.max_rows", None)
pd.set_option("display.width", 160)

print("\n" + "=" * 70)
print("STATISTICAL VALIDATION RESULTS")
print("=" * 70)

display_columns = [
    "Variable",
    "Test",
    "P_Value_Display",
    "Adjusted_P_Value_Display",
    "Effect_Size",
    "Effect_Strength",
    "Significant"
]

print(
    results[display_columns].to_string(index=False)
)

# =========================================================
# 12. SIGNIFICANT VARIABLES
# =========================================================

significant_results = results[
    results["Significant"]
].copy()

print("\n" + "=" * 70)
print("STATISTICALLY SIGNIFICANT VARIABLES")
print("=" * 70)

print(
    significant_results[
        [
            "Variable",
            "Test",
            "Adjusted_P_Value_Display",
            "Effect_Size",
            "Effect_Strength"
        ]
    ].to_string(index=False)
)

print(
    f"\nNumber of statistically significant variables: "
    f"{len(significant_results)}"
)

# =========================================================
# 13. NON-SIGNIFICANT VARIABLES
# =========================================================

non_significant = results[
    ~results["Significant"]
].copy()

print("\n" + "=" * 70)
print("NON-SIGNIFICANT VARIABLES")
print("=" * 70)

print(
    non_significant[
        [
            "Variable",
            "Test",
            "Adjusted_P_Value_Display",
            "Effect_Size"
        ]
    ].to_string(index=False)
)

# =========================================================
# 14. SAVE COMPLETE RESULTS
# =========================================================

results.to_csv(
    "Statistical_Validation_Results.csv",
    index=False
)

print(
    "\nComplete results saved to:"
    "\nStatistical_Validation_Results.csv"
)

# =========================================================
# 15. SAVE SIGNIFICANT RESULTS
# =========================================================

significant_results.to_csv(
    "Statistically_Significant_Variables.csv",
    index=False
)

print(
    "\nSignificant variables saved to:"
    "\nStatistically_Significant_Variables.csv"
)
