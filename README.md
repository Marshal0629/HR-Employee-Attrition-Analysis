````markdown
# HR Employee Attrition Analysis

An end-to-end HR Data Analytics project analyzing employee attrition using Python, statistical validation, and Tableau Public.

---

## 📌 Project Overview

Employee attrition can lead to recruitment costs, loss of experienced employees, productivity disruption, and increased workload for remaining employees.

This project analyzes an HR Employee Attrition dataset to identify patterns and employee segments associated with higher observed attrition.

The analysis covers:

- Employee demographics
- Job-related factors
- Monthly income
- Overtime
- Job satisfaction
- Work-life balance
- Environment satisfaction
- Business travel
- Job level
- Years at company
- Job role
- Stock option level

The project combines exploratory data analysis, statistical validation, interaction analysis, and interactive Tableau dashboards to transform employee data into business insights.

---

## 🎯 Objectives

- Inspect and understand the HR dataset
- Clean and validate the data
- Create a documented data dictionary
- Perform exploratory data analysis
- Calculate key HR attrition KPIs
- Identify factors associated with employee attrition
- Analyze selected combinations of employee characteristics
- Statistically validate observed associations
- Build interactive Tableau dashboards
- Develop HR-focused business insights and recommendations

---

## 📊 Dataset

The project uses the HR Employee Attrition dataset.

### Dataset Details

| Metric | Value |
|---|---:|
| Employees | 1,470 |
| Original Columns | 35 |
| Cleaned Columns | 31 |
| Missing Values | 0 |
| Duplicate Rows | 0 |

### Target Variable

`Attrition`

- `Yes` → Employee left the organization
- `No` → Employee stayed in the organization

### Data Cleaning

The following columns were removed because they were not useful for the analysis:

- `EmployeeCount`
- `Over18`
- `StandardHours`
- `EmployeeNumber`

Potential numerical outliers were reviewed and retained because unusual observations do not necessarily represent data errors.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **SciPy**
- **Statsmodels**
- **Tableau Public**
- **Markdown**

---

## 🔄 Project Workflow

```text
Raw HR Dataset
      ↓
Data Inspection
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Data Dictionary
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Interaction Analysis
      ↓
Statistical Validation
      ↓
Business Insights
      ↓
HR Recommendations
      ↓
Tableau Dashboards
      ↓
Final Documentation
````

---

## 📈 Key HR KPIs

| KPI                             |  Value |
| ------------------------------- | -----: |
| Total Employees                 |  1,470 |
| Employees Who Left              |    237 |
| Employees Who Stayed            |  1,233 |
| Overall Observed Attrition Rate | 16.12% |
| Median Monthly Income           |  4,919 |
| Median Years at Company         |      5 |

---

# 🔎 Key Findings

## 1. Overtime

Employees who worked overtime had an observed attrition rate of **30.53%**, compared with **10.44%** among employees who did not work overtime.

This represents an approximately **2.9× higher observed attrition rate** among employees working overtime.

**Business signal:** Workload and overtime patterns should be investigated as part of employee retention analysis.

---

## 2. Early Tenure

Employees with **0–2 years at the company** had an observed attrition rate of **29.82%**.

Observed attrition by tenure:

| Years at Company | Attrition Rate |
| ---------------- | -------------: |
| 0–2 years        |         29.82% |
| 3–5 years        |         13.82% |
| 6–10 years       |         12.28% |
| 11–20 years      |          6.67% |
| 21+ years        |         12.12% |

**Business signal:** Early-tenure employees represent an important segment for retention investigation.

---

## 3. Job Role

Attrition varied considerably across job roles.

| Job Role                  | Attrition Rate |
| ------------------------- | -------------: |
| Sales Representative      |         39.76% |
| Laboratory Technician     |         23.94% |
| Human Resources           |         23.08% |
| Sales Executive           |         17.48% |
| Research Scientist        |         16.10% |
| Manufacturing Director    |          6.90% |
| Healthcare Representative |          6.87% |
| Manager                   |          4.90% |
| Research Director         |          2.50% |

**Business signal:** Retention analysis should consider role-specific conditions rather than relying only on organization-wide attrition.

---

## 4. Monthly Income

Employees in the lowest income quartile had an observed attrition rate of **29.27%**, compared with **10.33%** in the highest income quartile.

| Income Group | Attrition Rate |
| ------------ | -------------: |
| Q1 – Lowest  |         29.27% |
| Q2           |         14.21% |
| Q3           |         10.63% |
| Q4 – Highest |         10.33% |

**Business signal:** Compensation should be investigated alongside workload, tenure, job level, and job role.

---

## 5. Business Travel

Employees who travelled frequently had an observed attrition rate of **24.91%**.

| Business Travel   | Attrition Rate |
| ----------------- | -------------: |
| Non-Travel        |          8.00% |
| Travel_Rarely     |         14.96% |
| Travel_Frequently |         24.91% |

**Business signal:** Frequent business travel may warrant additional HR investigation.

---

# 🔗 Interaction Analysis

Selected combinations of employee characteristics were analyzed to identify higher-observed-attrition segments.

### Early Tenure + Overtime

Employees with **0–2 years at the company who worked overtime** had an observed attrition rate of:

**50.96%**

---

### Lowest Income + Overtime

Employees in the **Q1 – Lowest Income + Overtime** group had an observed attrition rate of:

**58.49%**

---

### Job Role + Overtime

Selected observed attrition rates among employees working overtime:

| Job Role              | Attrition Rate |
| --------------------- | -------------: |
| Sales Representative  |         66.67% |
| Laboratory Technician |         50.00% |
| Human Resources       |         38.46% |
| Research Scientist    |         34.02% |
| Sales Executive       |         32.98% |

The Sales Representative + Overtime subgroup contains 24 employees, so the percentage should be interpreted as a potential risk signal requiring further investigation.

---

# 📐 Statistical Validation

Statistical validation was performed to determine whether observed differences in attrition were statistically significant.

### Methods Used

* **Chi-square test of independence** — categorical variables
* **Mann-Whitney U test** — continuous variables
* **Cramér's V** — categorical effect size
* **Rank-biserial correlation** — numerical effect size
* **Benjamini-Hochberg FDR correction** — multiple testing correction

### Validation Summary

* **29 variables tested**
* **20 remained statistically significant after FDR correction**

### Variables with Larger Effect Sizes

| Variable             | Effect Size | Effect Strength |
| -------------------- | ----------: | --------------- |
| TotalWorkingYears    |       0.312 | Large           |
| MonthlyIncome        |       0.311 | Large           |
| YearsAtCompany       |       0.298 | Moderate        |
| YearsInCurrentRole   |       0.280 | Moderate        |
| YearsWithCurrManager |       0.272 | Moderate        |
| Age                  |       0.269 | Moderate        |
| OverTime             |       0.244 | Moderate        |
| JobRole              |       0.242 | Moderate        |
| JobLevel             |       0.222 | Moderate        |
| StockOptionLevel     |       0.203 | Moderate        |

Statistical significance indicates evidence of association and does not establish causation.

---

# 🔗 Interaction Statistical Validation

Three interaction groupings were statistically validated:

* Years at Company × Overtime
* Income Group × Overtime
* Job Role × Overtime

All three were statistically significant after FDR correction.

| Interaction                 | Effect Size | Effect Strength |
| --------------------------- | ----------: | --------------- |
| Years at Company × Overtime |       0.337 | Moderate        |
| Income Group × Overtime     |       0.358 | Moderate        |
| Job Role × Overtime         |       0.377 | Moderate        |

The interaction validation used **combined categorical groups** and does not constitute a formal regression interaction-term test.

---

# 💡 Business Recommendations

Based on the observed patterns, the following areas are recommended for HR investigation:

### 1. Review Overtime and Workload

* Monitor recurring overtime
* Review workload distribution
* Identify teams with sustained overtime
* Evaluate staffing requirements

### 2. Strengthen Early-Tenure Support

* Improve onboarding
* Introduce mentoring
* Conduct regular manager check-ins
* Provide career-development discussions

### 3. Review Lower-Income Employee Segments

Investigate compensation, workload, job level, and career progression among lower-income employee groups, particularly employees also working overtime.

### 4. Develop Role-Specific Retention Strategies

Investigate workload, compensation, career progression, job satisfaction, and management support within higher-observed-attrition roles.

### 5. Review Business Travel

Investigate travel frequency, scheduling, workload during travel, employee support, and recovery time.

---

# 📊 Tableau Dashboard

The project includes two interactive Tableau Public dashboards.

### Dashboard 1 — HR Employee Attrition Dashboard

Includes:

* Total Employees
* Employees Who Left
* Employees Who Stayed
* Overall Attrition Rate
* Attrition by Overtime
* Attrition by Years at Company
* Attrition by Job Role
* Attrition by Income Group
* Attrition by Business Travel
* Attrition by Stock Option Level

Filters:

* Department
* Gender
* Job Role

### Dashboard 2 — Attrition Risk & Interaction Analysis

Includes:

* Years at Company × Overtime
* Income Group × Overtime
* Job Role × Overtime

### Tableau Public

[View the Interactive Tableau Dashboard](https://public.tableau.com/views/HREmployeeAttritionDashboard_17878437847440/HREmployeeAttritionDashboard)

---

# 📁 Project Structure

```text
HR-Employee-Attrition-Analysis/
│
├── 01_data_inspection.py
├── 02_data_cleaning.py
├── 03_validate_cleaned_data.py
├── 04_eda.py
├── 05_prepare_tableau_data.py
├── 06_statistical_validation.py
├── 07_interaction_validation.py
│
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── HR_Employee_Attrition_Cleaned.csv
├── HR_Employee_Attrition_Tableau.csv
│
├── Statistical_Validation_Results.csv
├── Statistically_Significant_Variables.csv
├── Interaction_Validation_Results.csv
│
├── Data_Dictionary.md
├── Data_Cleaning_Report.md
├── EDA_Findings.md
├── Business_Insights.md
├── Final_Project_Report.md
└── README.md
```

---

# 📚 Documentation

| File                      | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| `Data_Dictionary.md`      | Dataset variables, data types, categories, and removed columns         |
| `Data_Cleaning_Report.md` | Data-quality checks and cleaning process                               |
| `EDA_Findings.md`         | Exploratory analysis, interaction analysis, and statistical validation |
| `Business_Insights.md`    | Business insights and HR recommendations                               |
| `Final_Project_Report.md` | Complete end-to-end project report                                     |

---

# ⚠️ Analytical Limitations

* The dataset is observational, so associations should not be interpreted as causal relationships.
* The dataset does not include detailed information about individual reasons for leaving.
* Some employee segments contain relatively small numbers of observations.
* The analysis does not use a multivariable predictive model.
* Interaction validation used combined categorical groups rather than formal regression interaction terms.
* Results reflect the employee population represented in the dataset and may not generalize to another organization or workforce.

---

# 🏁 Conclusion

This project demonstrates an end-to-end HR analytics workflow using **Python, statistical validation, and Tableau Public**.

The analysis identified several employee characteristics and combined segments associated with higher observed attrition, including:

* Overtime
* Early tenure
* Monthly income
* Job role
* Business travel
* Job satisfaction
* Work-life balance
* Environment satisfaction
* Stock option level

The analysis found that **20 of 29 tested variables remained statistically significant after FDR correction**.

Interaction validation also identified statistically significant associations for:

* Years at Company × Overtime
* Income Group × Overtime
* Job Role × Overtime

The project transforms raw HR employee data into documented analytical findings, interactive dashboards, and business recommendations that can support further HR investigation.

---

## 👤 Author

**Marshal**

B.Tech Information Technology
Jeppiaar Engineering College
Anna University

---

## 📌 Disclaimer

This project is intended for educational and analytical purposes.

Observed relationships represent associations within the analyzed dataset and should not be interpreted as proof of causation or as a direct prediction of individual employee behavior.

```
