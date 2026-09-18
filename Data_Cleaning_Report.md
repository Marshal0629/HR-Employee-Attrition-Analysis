# Data Cleaning Report

## 1. Dataset Overview

- Dataset: IBM HR Employee Attrition
- Original records: 1,470
- Original columns: 35
- Objective: Identify factors associated with employee attrition.

## 2. Data Quality Assessment

### Missing Values
No missing values were found in any of the 35 columns.

**Action:** No treatment required.

### Duplicate Records
No duplicate rows were identified.

**Action:** No records removed.

### Constant Columns
The following columns contained only one unique value:

- EmployeeCount
- Over18
- StandardHours

**Action:** Removed from the analysis dataset because they provide no variation.

### Employee Identifier
`EmployeeNumber` contained a unique value for every employee.

**Action:** Removed from the analysis dataset because it is an identifier and does not provide a meaningful explanatory factor for attrition.

### Categorical Variables
Categorical variables were inspected for inconsistent or unexpected values. No obvious inconsistencies were identified.

**Action:** No cleaning required.

### Numerical Variables
Numerical variables were inspected using descriptive statistics and range checks. No obvious invalid values were identified.

**Action:** No cleaning required.

### Logical Consistency
The following relationships were checked:

- YearsAtCompany <= TotalWorkingYears
- YearsInCurrentRole <= YearsAtCompany
- YearsWithCurrManager <= YearsAtCompany
- YearsSinceLastPromotion <= YearsAtCompany

No violations were found.

**Action:** No cleaning required.

### Potential Outliers
IQR-based screening identified potential statistical outliers in several variables.

These observations were retained because statistical unusualness alone does not indicate data-entry error.

**Action:** No records removed based solely on outlier detection.

## 3. Cleaning Summary

| Item | Result |
|---|---|
| Original rows | 1,470 |
| Original columns | 35 |
| Rows removed | 0 |
| Columns removed | 4 |
| Final rows | 1,470 |
| Final columns | 31 |

## 4. Removed Columns

| Column | Reason |
|---|---|
| EmployeeCount | Constant value across all employees |
| Over18 | Constant value across all employees |
| StandardHours | Constant value across all employees |
| EmployeeNumber | Unique employee identifier, not an explanatory variable |