# HR Employee Attrition Analysis

## Project Overview

### Project Objective

The objective of this project is to analyze employee attrition data, identify the key factors and employee segments associated with higher attrition, and develop actionable insights that can help Human Resources improve employee retention.

### Business Problem

Employee turnover can create significant challenges for an organization, including recruitment costs, loss of experienced employees, reduced productivity, and disruption to teams.

This project uses employee-level HR data to understand where attrition is concentrated and identify patterns that HR can investigate and address through targeted retention strategies.

### Dataset

The analysis uses the HR Employee Attrition dataset containing records for **1,470 employees**.

The original dataset contains employee demographic, job-related, compensation, satisfaction, work-life, and organizational information, along with an `Attrition` indicator showing whether an employee left the organization.

---

## Tools Used

- **Python** — Data inspection, cleaning, validation, feature engineering, exploratory data analysis, and statistical analysis
- **Pandas** — Data manipulation and analysis
- **SciPy** — Statistical hypothesis testing
- **Statsmodels** — Multiple-testing correction using the Benjamini-Hochberg False Discovery Rate procedure
- **Tableau Public** — Data visualization and interactive dashboard development
- **Markdown** — Project documentation

---

## Project Workflow

The project followed the following analytical workflow:

1. Dataset inspection
2. Data cleaning and validation
3. Data dictionary preparation
4. Feature engineering
5. Exploratory Data Analysis (EDA)
6. Individual statistical validation
7. Interaction analysis
8. Interaction statistical validation
9. Identification and documentation of key findings
10. Business insight development
11. HR recommendation development
12. Tableau dashboard development
13. Tableau Public publication
14. Final project consistency review

---

# Data Preparation & Methodology

## Data Inspection

The dataset was initially inspected to understand its structure, dimensions, data types, available variables, unique values, and potential data-quality issues.

The original dataset contains:

- **1,470 employee records**
- **35 columns**

The target variable for the analysis is `Attrition`, which indicates whether an employee left the organization.

The inspection process also included checks for:

- Missing values
- Duplicate records
- Categorical values
- Numerical summaries
- Logical consistency between related employee-tenure variables
- Potential numerical outliers

---

## Data Cleaning

The data-cleaning process focused on removing fields that were not useful for employee attrition analysis while preserving the employee-level information required for the project.

The following columns were removed:

- `EmployeeCount`
- `Over18`
- `StandardHours`
- `EmployeeNumber`

The original dataset contained:

- **1,470 rows**
- **35 columns**

The cleaned dataset contains:

- **1,470 rows**
- **31 columns**

### Data Quality Validation

The cleaned dataset was validated for:

- Missing values
- Duplicate rows
- Removed columns
- Data consistency

The cleaned dataset contains:

- **0 missing values**
- **0 duplicate rows**

Potential numerical outliers were identified during inspection but were retained because unusual values do not necessarily represent data errors.

Logical consistency checks were also performed for related tenure variables, including:

- YearsAtCompany ≤ TotalWorkingYears
- YearsInCurrentRole ≤ YearsAtCompany
- YearsWithCurrManager ≤ YearsAtCompany
- YearsSinceLastPromotion ≤ YearsAtCompany

No logical consistency violations were identified.

---

## Data Dictionary

A separate `Data_Dictionary.md` file was created to document the dataset variables.

The dictionary describes:

- Variable names
- Variable meanings
- Data types
- Numerical variables
- Categorical variables
- Ordinal variables
- Removed columns

This provides a reference for understanding the dataset and the analytical variables used throughout the project.

---

# Feature Engineering

Additional analytical fields were created to make the dataset easier to analyze and visualize.

## Income Group

Monthly Income was divided into four quartile-based groups:

- **Q1 – Lowest**
- **Q2**
- **Q3**
- **Q4 – Highest**

This grouping was used to compare observed attrition across different income levels.

## Years at Company Group

Employees were grouped according to their YearsAtCompany:

- **0–2 years**
- **3–5 years**
- **6–10 years**
- **11–20 years**
- **21+ years**

This grouping was used to analyze attrition across different tenure stages.

These derived fields were also included in the Tableau-ready dataset.

---

# Exploratory Data Analysis

Exploratory Data Analysis was performed using Python and Pandas to examine the relationship between employee attrition and multiple employee characteristics.

The analysis included:

- Overall attrition
- Attrition by overtime
- Attrition by job level
- Attrition by job satisfaction
- Attrition by monthly income group
- Attrition by years at company
- Attrition by job role
- Attrition by work-life balance
- Attrition by environment satisfaction
- Attrition by stock option level
- Attrition by business travel

---

## Key HR KPIs

The overall employee population was:

| KPI | Value |
|---|---:|
| Total Employees | 1,470 |
| Employees Who Left | 237 |
| Employees Who Stayed | 1,233 |
| Overall Observed Attrition Rate | 16.12% |
| Median Monthly Income | 4,919 |
| Median Years at Company | 5 |

The overall observed attrition rate was calculated as:

**237 ÷ 1,470 × 100 = 16.12%**

---

# Major EDA Findings

## 1. Overtime

Employees who worked overtime had an observed attrition rate of **30.53%**, compared with **10.44%** among employees who did not work overtime.

This represents an approximately **2.9× higher observed attrition rate** among employees who worked overtime.

**Key takeaway:** Overtime is an important actionable HR risk signal associated with employee attrition.

This result shows an association and does not by itself establish that overtime causes employees to leave.

---

## 2. Job Level

Observed attrition rates varied across Job Levels:

| Job Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 26.34% |
| Level 2 | 9.74% |
| Level 3 | 14.68% |
| Level 4 | 4.72% |
| Level 5 | 7.25% |

Job Level 1 had the highest observed attrition rate at **26.34%**, while Level 4 had the lowest at **4.72%**.

The relationship was not perfectly linear across all levels.

---

## 3. Job Satisfaction

Observed attrition rates by Job Satisfaction were:

| Job Satisfaction Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 22.84% |
| Level 2 | 16.43% |
| Level 3 | 16.52% |
| Level 4 | 11.33% |

Employees with the lowest Job Satisfaction level had the highest observed attrition rate.

The pattern generally indicates higher observed attrition among employees with lower Job Satisfaction.

---

## 4. Monthly Income

Observed attrition rates by income group were:

| Income Group | Observed Attrition Rate |
|---|---:|
| Q1 – Lowest | 29.27% |
| Q2 | 14.21% |
| Q3 | 10.63% |
| Q4 – Highest | 10.33% |

Employees in the lowest income quartile had an observed attrition rate of **29.27%**, compared with **10.33%** among employees in the highest income quartile.

**Key takeaway:** Lower income is strongly associated with higher observed attrition in this dataset.

---

## 5. Years at Company

Observed attrition rates by tenure group were:

| Years at Company | Observed Attrition Rate |
|---|---:|
| 0–2 years | 29.82% |
| 3–5 years | 13.82% |
| 6–10 years | 12.28% |
| 11–20 years | 6.67% |
| 21+ years | 12.12% |

Employees with **0–2 years** at the company had the highest observed attrition rate at **29.82%**.

The results indicate that early-tenure employees represent an important attrition segment.

---

## 6. Job Role

Observed attrition rates varied substantially across Job Roles.

| Job Role | Observed Attrition Rate |
|---|---:|
| Sales Representative | 39.76% |
| Laboratory Technician | 23.94% |
| Human Resources | 23.08% |
| Sales Executive | 17.48% |
| Research Scientist | 16.10% |
| Manufacturing Director | 6.90% |
| Healthcare Representative | 6.87% |
| Manager | 4.90% |
| Research Director | 2.50% |

Sales Representatives had the highest observed attrition rate at **39.76%**.

**Key takeaway:** Attrition is not evenly distributed across job roles.

---

## 7. Work-Life Balance

Observed attrition rates by WorkLifeBalance level were:

| Work-Life Balance Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 31.25% |
| Level 2 | 16.86% |
| Level 3 | 14.22% |
| Level 4 | 17.65% |

Level 1 had the highest observed attrition rate.

The relationship was not perfectly linear because Level 4 had a higher observed attrition rate than Level 3.

---

## 8. Environment Satisfaction

Observed attrition rates by Environment Satisfaction were:

| Environment Satisfaction Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 25.35% |
| Level 2 | 14.98% |
| Level 3 | 13.69% |
| Level 4 | 13.45% |

The lowest Environment Satisfaction level had the highest observed attrition rate.

---

## 9. Stock Option Level

Observed attrition rates by Stock Option Level were:

| Stock Option Level | Observed Attrition Rate |
|---|---:|
| Level 0 | 24.41% |
| Level 1 | 9.40% |
| Level 2 | 7.59% |
| Level 3 | 17.65% |

Employees at Stock Option Level 0 had the highest observed attrition rate.

The relationship was U-shaped rather than consistently linear across all levels.

---

## 10. Business Travel

Observed attrition rates by Business Travel were:

| Business Travel | Observed Attrition Rate |
|---|---:|
| Non-Travel | 8.00% |
| Travel_Rarely | 14.96% |
| Travel_Frequently | 24.91% |

Employees who travelled frequently had the highest observed attrition rate at **24.91%**.

**Key takeaway:** Frequent business travel is associated with substantially higher observed attrition.

---

# Interaction Analysis

After analyzing individual employee characteristics, selected variables were combined to identify potentially higher-risk employee segments.

The following combinations were examined:

- Years at Company × Overtime
- Income Group × Overtime
- Job Role × Overtime
- Job Role × Income Group

The interaction analysis was used to identify employee groups where multiple characteristics occurred together with higher observed attrition.

---

## Early Tenure + Overtime

Employees with **0–2 years at the company who worked overtime** had an observed attrition rate of:

**50.96%**

Among employees with 0–2 years who did not work overtime, the observed attrition rate was:

**20.59%**

This identifies early-tenure employees working overtime as an important employee segment for HR investigation.

---

## Lowest Income + Overtime

Employees in the **Q1 – Lowest income group who worked overtime** had an observed attrition rate of:

**58.49%**

Among employees in the same income group who did not work overtime, the observed attrition rate was:

**17.49%**

Among overtime employees, observed attrition rates by income group were:

- Q1 – Lowest: **58.49%**
- Q2: **26.04%**
- Q3: **19.27%**
- Q4 – Highest: **18.10%**

This represents an important combined risk signal in the dataset.

---

## Job Role + Overtime

Among employees who worked overtime, selected job roles showed the following observed attrition rates:

| Job Role | Observed Attrition Rate |
|---|---:|
| Sales Representative | 66.67% |
| Laboratory Technician | 50.00% |
| Human Resources | 38.46% |
| Research Scientist | 34.02% |
| Sales Executive | 32.98% |

The Sales Representative + Overtime subgroup contains **24 employees**, so its 66.67% observed attrition rate should be interpreted as a potential risk signal rather than a definitive estimate.

Laboratory Technicians had a 50.00% observed attrition rate among **62 overtime employees**, providing a larger subgroup for comparison.

---

# Statistical Validation

Statistical validation was performed to determine whether observed differences in attrition were statistically significant.

The analysis used:

- **Chi-square test of independence** for categorical variables
- **Mann-Whitney U test** for continuous numerical variables
- **Cramér's V** for categorical effect size
- **Rank-biserial correlation** for numerical effect size
- **Benjamini-Hochberg False Discovery Rate (FDR) correction** for multiple testing

A significance threshold of **0.05 after FDR correction** was used.

A total of **29 variables were tested**, of which **20 remained statistically significant after FDR correction**.

---

## Variables with the Largest Effect Sizes

| Variable | Statistical Test | Effect Size | Effect Strength |
|---|---|---:|---|
| TotalWorkingYears | Mann-Whitney U | 0.312 | Large |
| MonthlyIncome | Mann-Whitney U | 0.311 | Large |
| YearsAtCompany | Mann-Whitney U | 0.298 | Moderate |
| YearsInCurrentRole | Mann-Whitney U | 0.280 | Moderate |
| YearsWithCurrManager | Mann-Whitney U | 0.272 | Moderate |
| Age | Mann-Whitney U | 0.269 | Moderate |
| OverTime | Chi-square | 0.244 | Moderate |
| JobRole | Chi-square | 0.242 | Moderate |
| JobLevel | Chi-square | 0.222 | Moderate |
| StockOptionLevel | Chi-square | 0.203 | Moderate |

These results provide statistical support for several of the patterns identified during EDA.

Statistical significance indicates evidence of an association, not causation.

Statistical significance and practical importance are also different concepts. Therefore, statistical results were considered alongside observed attrition rates and business relevance.

---

## Other Statistically Significant Variables

The following variables also remained statistically significant after FDR correction:

- MaritalStatus
- JobInvolvement
- BusinessTravel
- EnvironmentSatisfaction
- JobSatisfaction
- WorkLifeBalance
- DistanceFromHome
- Department
- EducationField
- DailyRate

These variables were statistically associated with attrition in the analyzed dataset.

---

## Variables Not Statistically Significant After FDR Correction

The following variables did not remain statistically significant after FDR correction:

- YearsSinceLastPromotion
- RelationshipSatisfaction
- NumCompaniesWorked
- Gender
- PercentSalaryHike
- Education
- MonthlyRate
- HourlyRate
- PerformanceRating

These variables were therefore not emphasized as statistically supported factors in the final analysis.

---

# Interaction Statistical Validation

Selected combined employee groups were statistically validated to determine whether the interaction groupings were associated with attrition.

The following interaction groupings were tested:

- Years at Company × Overtime
- Income Group × Overtime
- Job Role × Overtime

All three interaction groupings were statistically significant after Benjamini-Hochberg FDR correction.

| Interaction | Effect Size | Effect Strength |
|---|---:|---|
| Years at Company × Overtime | 0.337 | Moderate |
| Income Group × Overtime | 0.358 | Moderate |
| Job Role × Overtime | 0.377 | Moderate |

The results provide statistical support for the observation that attrition varies across combined employee segments.

Examples of high observed attrition segments include:

- **0–2 years + Overtime: 50.96%**
- **Q1 – Lowest Income + Overtime: 58.49%**
- **Sales Representative + Overtime: 66.67%**

The interaction validation used **combined categorical groups** and therefore does not constitute a formal regression interaction-term test.

The results identify associations between combined employee characteristics and attrition rather than causal effects.

---

# Business Insights

The analysis identified several recurring patterns that are relevant for HR investigation.

## Workload

Employees working overtime showed substantially higher observed attrition than employees who did not work overtime.

This indicates that workload management is an important area for HR investigation.

## Early-Tenure Retention

Employees with 0–2 years at the company showed substantially higher observed attrition than most longer-tenure groups.

This suggests that onboarding, early-career support, workload, and employee experience during the first few years may warrant further investigation.

## Compensation

Employees in the lowest income quartile showed substantially higher observed attrition than employees in the higher income quartiles.

Compensation should therefore be considered alongside job level, role, tenure, and overtime when investigating retention.

## Job-Specific Retention

Attrition varied considerably across job roles.

Certain roles showed substantially higher observed attrition, indicating that role-specific workload, career development, compensation, and working conditions may warrant further investigation.

## Business Travel

Employees who travelled frequently showed higher observed attrition than employees who travelled rarely or did not travel.

Travel frequency, scheduling, workload, and employee support may therefore be relevant areas for HR review.

## Combined Risk Signals

The interaction analysis showed that some employee groups experienced substantially higher observed attrition when multiple characteristics occurred together.

Examples include:

- Early tenure + overtime
- Lowest income + overtime
- Specific job roles + overtime

These combined segments can help HR focus further investigation on specific employee populations rather than relying only on overall attrition.

---

# HR Recommendations

The recommendations below are based on observed patterns in the dataset and are intended as areas for HR investigation rather than guaranteed solutions.

## 1. Review Overtime and Workload

HR can investigate overtime patterns by department, job role, tenure, and income group.

Potential actions include:

- Reviewing workload distribution
- Monitoring recurring overtime
- Identifying teams with sustained overtime
- Evaluating staffing requirements
- Discussing workload concerns with affected employees

## 2. Strengthen Early-Tenure Support

Because employees with 0–2 years at the company showed higher observed attrition, HR can investigate early-tenure employee experience.

Potential actions include:

- Structured onboarding
- Early-career mentoring
- Regular manager check-ins
- Career-development discussions
- Workload reviews during the first few years

## 3. Review Lower-Income Employee Segments

The lowest income quartile showed higher observed attrition, particularly when combined with overtime.

HR can investigate whether workload, compensation, job level, and career progression are appropriately aligned for these employees.

## 4. Develop Role-Specific Retention Strategies

Because attrition varies across job roles, HR can investigate the specific conditions associated with higher attrition roles.

Potential areas include:

- Workload
- Overtime
- Compensation
- Career progression
- Job satisfaction
- Management support

## 5. Review Business Travel Requirements

Employees who travelled frequently showed higher observed attrition.

HR can review:

- Travel frequency
- Scheduling
- Workload during travel periods
- Employee support
- Recovery time after travel

---

# Tableau Dashboard & Visualization

The analytical findings were presented through an interactive Tableau Public dashboard.

The published workbook contains two main dashboards.

## Dashboard 1 — HR Employee Attrition Dashboard

The main dashboard provides an overview of employee attrition.

### KPI Cards

- **Total Employees:** 1,470
- **Employees Who Left:** 237
- **Employees Who Stayed:** 1,233
- **Overall Attrition Rate:** 16.12%

### Main Visualizations

- Attrition by Overtime
- Attrition by Years at Company
- Attrition by Job Role
- Attrition by Income Group
- Attrition by Business Travel
- Attrition by Stock Option Level

### Filters

- Department
- Gender
- Job Role

These filters allow users to explore attrition patterns across different employee segments.

---

## Dashboard 2 — Attrition Risk & Interaction Analysis

The second dashboard focuses on combined employee characteristics.

It includes:

- Years at Company × Overtime
- Income Group × Overtime
- Job Role × Overtime

This dashboard provides an interactive view of the employee segments identified during the interaction analysis.

The Tableau dashboards complement the Python analysis by allowing users to visually explore the major attrition patterns.

---

# Project Deliverables

The completed project contains the following analytical and documentation outputs:

### Data and Preparation

- Original HR employee attrition dataset
- Cleaned HR employee attrition dataset
- Tableau-ready dataset
- Data dictionary
- Data cleaning report

### Analysis

- Data inspection script
- Data cleaning script
- Cleaned-data validation script
- EDA script
- Tableau data preparation script
- Statistical validation script
- Interaction validation script

### Results

- Statistical validation results
- Statistically significant variables
- Interaction validation results
- EDA findings
- Business insights and recommendations

### Visualization

- Interactive Tableau dashboard
- Tableau Public publication

### Documentation

- Final project report
- Supporting analytical documentation

---

# Analytical Limitations

The findings from this project should be interpreted within the limitations of the available dataset and analytical approach.

## 1. Observational Data

The analysis is based on historical employee data.

The observed relationships identify associations between employee characteristics and attrition but do not establish causal relationships.

For example, the analysis shows that overtime is associated with higher attrition, but it cannot independently prove that overtime causes employees to leave.

## 2. Limited Organizational Context

The dataset does not provide detailed information about factors such as:

- Manager effectiveness
- Employee engagement
- Individual reasons for leaving
- External job opportunities
- Organizational culture
- Compensation competitiveness against the external market

These factors may also influence employee attrition.

## 3. Smaller Employee Segments

Some employee groups contain relatively few employees.

Their attrition percentages can therefore be more sensitive to a small number of employee departures.

Examples include certain job roles, stock option levels, and interaction groups.

These segments should be interpreted as potential risk signals requiring further investigation rather than definitive conclusions.

## 4. Statistical Analysis

Statistical validation identifies evidence of association but does not establish causality.

The analysis also does not use a multivariable predictive model to estimate whether each factor independently predicts attrition after controlling for all other employee characteristics.

## 5. Interaction Analysis

The interaction validation used combined categorical employee groups and statistical association tests.

It did not estimate formal regression interaction terms.

Therefore, the interaction results should be interpreted as evidence of association between combined employee characteristics and observed attrition.

## 6. Historical Dataset

The analysis reflects the employee population represented in the dataset and may not necessarily represent the current workforce or another organization.

---

# Conclusion

This project analyzed employee attrition across demographic, job-related, compensation, satisfaction, work-life, and organizational factors.

The overall observed attrition rate was **16.12%**, with **237 of 1,470 employees** represented in the dataset having left the organization.

The exploratory analysis identified several important patterns. Overtime, early tenure, lower income, specific job roles, frequent business travel, and certain employee satisfaction and benefit levels were associated with higher observed attrition.

The interaction analysis provided additional insight into combined employee segments.

In particular:

- Employees with **0–2 years at the company + Overtime** had an observed attrition rate of **50.96%**.
- Employees in the **Q1 – Lowest Income + Overtime** group had an observed attrition rate of **58.49%**.
- **Sales Representatives + Overtime** had an observed attrition rate of **66.67%**, although this subgroup contains only 24 employees.

Statistical validation provided additional evidence for several individual factors.

Out of **29 variables tested, 20 remained statistically significant after FDR correction**.

The largest effect sizes among the tested variables included TotalWorkingYears, MonthlyIncome, YearsAtCompany, YearsInCurrentRole, YearsWithCurrManager, Age, OverTime, JobRole, JobLevel, and StockOptionLevel.

Interaction statistical validation also found statistically significant associations for:

- Years at Company × Overtime
- Income Group × Overtime
- Job Role × Overtime

These findings should be interpreted as associations within the analyzed dataset rather than causal relationships.

The Tableau dashboards provide an interactive way to explore the observed attrition patterns, while the Python analysis and statistical validation provide the underlying analytical evidence.

Overall, the project demonstrates how HR employee data can be transformed into **data-driven business insights and actionable areas for retention investigation**.

---

# Project Outcome

The completed project delivers:

- A cleaned and validated HR dataset
- A documented data dictionary
- Engineered analytical features
- Comprehensive exploratory data analysis
- Interaction analysis of selected employee segments
- Statistical validation of individual variables
- Statistical validation of selected interaction groupings
- Documented EDA findings
- Business insights and HR recommendations
- An interactive Tableau dashboard
- A second Tableau dashboard focused on interaction analysis
- A published Tableau Public visualization
- A structured final project report

The project provides a foundation for further HR analytics work, including:

- Predictive attrition modeling
- Employee risk scoring
- Formal multivariable regression analysis
- Formal regression interaction modeling
- Deeper investigation of the underlying reasons for employee turnover

Predictive machine learning was outside the required scope of this project and was therefore not included in the completed analytical workflow.
