# EDA Findings

## Baseline Attrition

The dataset contains **1,470 employees**.

- Employees who left: **237**
- Employees who stayed: **1,233**
- Overall observed attrition rate: **16.12%**

The overall attrition rate of 16.12% provides the baseline against which the attrition rates of different employee groups were compared.

---

## Finding 1 — Overtime

Employees who worked overtime had an observed attrition rate of **30.53%**, compared with **10.44%** among employees who did not work overtime.

This represents an approximately **2.9× higher** observed attrition rate among employees who worked overtime.

**Interpretation:** Overtime is an important factor associated with employee attrition and represents an actionable HR risk signal.

**Caution:** This result shows an association and does not by itself prove that overtime causes employees to leave.

---

## Finding 2 — Job Level

Employees at different job levels showed different observed attrition rates.

| Job Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 26.34% |
| Level 2 | 9.74% |
| Level 3 | 14.68% |
| Level 4 | 4.72% |
| Level 5 | 7.25% |

Job Level 1 had the highest observed attrition rate at **26.34%**, while Job Level 4 had the lowest at **4.72%**.

Lower job levels, particularly Level 1, showed higher observed attrition than most higher job levels.

**Interpretation:** Job Level appears to be an important factor associated with employee attrition and should be considered alongside factors such as income, overtime, tenure, and job role.

**Caution:** The pattern is not perfectly linear. Job Level 3 has a higher attrition rate than Level 2, and Level 5 has a higher rate than Level 4. The Level 5 group also contains only 69 employees, so its percentage should be interpreted with greater caution.

This analysis shows an association and does not prove that Job Level causes employees to leave.

---

## Finding 3 — Job Satisfaction

Employees with different levels of Job Satisfaction showed different observed attrition rates.

| Job Satisfaction Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 22.84% |
| Level 2 | 16.43% |
| Level 3 | 16.52% |
| Level 4 | 11.33% |

Employees with Job Satisfaction level 1 had the highest observed attrition rate at **22.84%**, while level 4 had the lowest at **11.33%**.

There is an overall downward pattern, although Level 3 was slightly higher than Level 2 by only 0.09 percentage points.

**Interpretation:** Lower Job Satisfaction appears to be associated with higher employee attrition.

**Caution:** This analysis shows an association and does not prove that low Job Satisfaction causes employees to leave.

---

## Finding 4 — Monthly Income

Monthly income was divided into four quartile-based groups:

- Q1 — Lowest
- Q2
- Q3
- Q4 — Highest

The observed attrition rates were:

| Income Group | Observed Attrition Rate |
|---|---:|
| Q1 — Lowest | 29.27% |
| Q2 | 14.21% |
| Q3 | 10.63% |
| Q4 — Highest | 10.33% |

Employees in the lowest monthly income quartile had an observed attrition rate of **29.27%**, compared with **10.33%** among employees in the highest income quartile.

Attrition was substantially higher in the lowest income group, while the higher income groups showed considerably lower and relatively similar attrition rates.

**Interpretation:** Monthly Income appears to be an important factor associated with employee attrition, particularly for employees in the lowest income group.

**Caution:** The relationship is not interpreted as a direct causal effect. Other factors such as Job Level, Job Role, Age, Tenure, and Overtime may also be related to income and attrition.

This analysis shows an association and does not prove that lower income causes employees to leave.

---

## Finding 5 — Years at Company

Employees were grouped according to their Years at Company.

| Years at Company | Observed Attrition Rate |
|---|---:|
| 0–2 years | 29.82% |
| 3–5 years | 13.82% |
| 6–10 years | 12.28% |
| 11–20 years | 6.67% |
| 21+ years | 12.12% |

Employees with **0–2 years** at the company had the highest observed attrition rate at **29.82%**, while employees with **11–20 years** had the lowest rate at **6.67%**.

Attrition generally decreased as employees spent more years at the company, although the 21+ years group showed a slight increase to **12.12%**.

**Interpretation:** Years at Company appears to be an important factor associated with employee attrition, with early-tenure employees showing substantially higher observed attrition than employees with longer tenure.

**Caution:** The 21+ years group contains only 66 employees, so its higher attrition rate should be interpreted with greater caution. The analysis does not explain why early-tenure employees have higher attrition.

This analysis shows an association and does not establish causation.

---

## Finding 6 — Job Role

Attrition varied considerably across different job roles.

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

Sales Representatives had the highest observed attrition rate at **39.76%**, while Research Directors had the lowest at **2.50%**.

Laboratory Technicians (**23.94%**) and Human Resources employees (**23.08%**) also showed relatively high observed attrition.

**Interpretation:** Job Role appears to be an important factor associated with employee attrition, with Sales Representatives showing particularly high observed attrition.

**Caution:** Differences across job roles may also be related to other factors such as Overtime, Monthly Income, Job Level, and Years at Company. Smaller groups, such as Human Resources with 52 employees and Research Director with 80 employees, should also be interpreted with greater caution.

This analysis shows association and does not prove that Job Role itself causes employees to leave.

---

## Finding 7 — Work-Life Balance

Employees with different WorkLifeBalance levels showed different observed attrition rates.

| Work-Life Balance Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 31.25% |
| Level 2 | 16.86% |
| Level 3 | 14.22% |
| Level 4 | 17.65% |

Employees with WorkLifeBalance level 1 had the highest observed attrition rate at **31.25%**, while level 3 had the lowest at **14.22%**.

Attrition decreased from level 1 to level 3 but increased again at level 4, indicating that the relationship was not consistently linear.

**Interpretation:** WorkLifeBalance shows an association with employee attrition, particularly the higher observed attrition among employees in level 1.

**Caution:** The level 1 group contains only 80 employees, so its 31.25% attrition rate should be interpreted with greater caution.

This analysis shows an association and does not prove that WorkLifeBalance causes employees to leave.

---

## Finding 8 — Environment Satisfaction

Employees with different Environment Satisfaction levels showed different observed attrition rates.

| Environment Satisfaction Level | Observed Attrition Rate |
|---|---:|
| Level 1 | 25.35% |
| Level 2 | 14.98% |
| Level 3 | 13.69% |
| Level 4 | 13.45% |

Employees with Environment Satisfaction level 1 had the highest observed attrition rate at **25.35%**, while level 4 had the lowest at **13.45%**.

Attrition generally decreased as Environment Satisfaction increased, with the largest difference occurring between level 1 and the higher satisfaction levels.

**Interpretation:** Higher Environment Satisfaction appears to be associated with lower employee attrition.

**Caution:** Although the pattern is relatively consistent, this analysis shows an association and does not prove that Environment Satisfaction causes employees to leave.

---

## Finding 9 — Stock Option Level

Attrition varied considerably across Stock Option Levels.

| Stock Option Level | Observed Attrition Rate |
|---|---:|
| Level 0 | 24.41% |
| Level 1 | 9.40% |
| Level 2 | 7.59% |
| Level 3 | 17.65% |

Employees at Stock Option Level 0 had the highest observed attrition rate at **24.41%**, while Level 2 had the lowest at **7.59%**.

Attrition decreased sharply from Level 0 to Level 2 but increased again to **17.65%** at Level 3, resulting in a U-shaped pattern.

**Interpretation:** Stock Option Level appears to be an important factor associated with employee attrition, particularly the higher observed attrition among employees at Level 0.

**Caution:** The Level 3 group contains only 85 employees, so its 17.65% attrition rate should be interpreted with greater caution. The U-shaped pattern also indicates that the relationship is not simply linear.

This analysis shows an association and does not prove that Stock Option Level causes employees to leave.

---

## Finding 10 — Business Travel

Employees with different Business Travel frequencies showed different observed attrition rates.

| Business Travel | Observed Attrition Rate |
|---|---:|
| Non-Travel | 8.00% |
| Travel_Rarely | 14.96% |
| Travel_Frequently | 24.91% |

Employees who travelled frequently had the highest observed attrition rate at **24.91%**, while employees who did not travel had the lowest rate at **8.00%**.

Employees who travelled rarely had an attrition rate of **14.96%**.

**Interpretation:** Frequent business travel appears to be an important factor associated with employee attrition, with frequently travelling employees showing substantially higher observed attrition.

**Caution:** The Non-Travel group contains 150 employees, which is smaller than the Travel_Rarely and Travel_Frequently groups, so its rate should be interpreted with somewhat greater caution.

This analysis shows an association and does not prove that frequent business travel causes employees to leave.

---

# High-Risk Employee Segments

After analyzing individual factors, selected combinations of variables were examined to identify employee segments with substantially higher observed attrition.

## 1. Years at Company × Overtime

Observed attrition rates:

| Years at Company | Overtime | Observed Attrition Rate |
|---|---|---:|
| 0–2 years | Yes | 50.96% |
| 0–2 years | No | 20.59% |
| 3–5 years | Yes | 28.35% |
| 3–5 years | No | 7.82% |
| 6–10 years | Yes | 25.83% |
| 6–10 years | No | 7.32% |
| 11–20 years | Yes | 9.30% |
| 11–20 years | No | 5.84% |
| 21+ years | Yes | 13.64% |
| 21+ years | No | 11.36% |

The **0–2 years + Overtime** group had an observed attrition rate of **50.96%**.

**Interpretation:** The combination of early tenure and overtime identifies a segment with substantially higher observed attrition than the overall workforce.

**Caution:** This is an observed segment-level association and does not establish that early tenure combined with overtime causes employees to leave.

---

## 2. Income Group × Overtime

Observed attrition rates:

| Income Group | Overtime | Observed Attrition Rate |
|---|---|---:|
| Q1 — Lowest | Yes | 58.49% |
| Q1 — Lowest | No | 17.49% |
| Q2 | Yes | 26.04% |
| Q2 | No | 10.04% |
| Q3 | Yes | 19.27% |
| Q3 | No | 7.79% |
| Q4 — Highest | Yes | 18.10% |
| Q4 — Highest | No | 8.20% |

The **Q1 — Lowest Income + Overtime** group had an observed attrition rate of **58.49%**.

**Interpretation:** The combination of lower income and overtime identifies a segment with substantially higher observed attrition.

**Caution:** The result represents an association within the observed dataset. It does not prove that low income and overtime together cause employee attrition.

---

## 3. Job Role × Overtime

Selected observed attrition rates among employees working overtime included:

| Job Role | Overtime | Observed Attrition Rate |
|---|---|---:|
| Sales Representative | Yes | 66.67% |
| Laboratory Technician | Yes | 50.00% |
| Human Resources | Yes | 38.46% |
| Research Scientist | Yes | 34.02% |
| Sales Executive | Yes | 32.98% |

The **Sales Representative + Overtime** segment had an observed attrition rate of **66.67%**.

**Interpretation:** Attrition varies substantially across job roles when overtime status is considered.

**Caution:** Some role-overtime combinations contain relatively small numbers of employees. For example, the Sales Representative + Overtime group contains 24 employees. Therefore, these percentages should be treated as potential risk signals requiring further investigation rather than definitive conclusions.

---

# Consolidated EDA Insights

The exploratory analysis identified several recurring patterns:

1. **Overtime:** Employees working overtime had substantially higher observed attrition than employees not working overtime.
2. **Early Tenure:** Employees with 0–2 years at the company showed substantially higher observed attrition than most longer-tenure groups.
3. **Income:** Employees in the lowest income quartile showed considerably higher observed attrition than employees in the higher income quartiles.
4. **Job Role:** Attrition varied considerably across job roles, with Sales Representatives showing particularly high observed attrition.
5. **Business Travel:** Employees travelling frequently showed higher observed attrition than employees travelling rarely or not travelling.
6. **Work-Life Balance:** The lowest WorkLifeBalance level showed substantially higher observed attrition, although the overall relationship was not linear.
7. **Environment Satisfaction:** The lowest Environment Satisfaction level showed higher observed attrition than the higher satisfaction levels.
8. **Stock Options:** Stock Option Level 0 showed higher observed attrition, although the relationship was U-shaped rather than consistently linear.
9. **Job Level:** Lower job levels, particularly Level 1, showed higher observed attrition than most higher job levels.
10. **Job Satisfaction:** Lower Job Satisfaction was generally associated with higher observed attrition.

These findings were used to identify areas for further statistical validation and business interpretation.

---

# Statistical Validation

Statistical validation was performed to determine whether observed differences in attrition were statistically significant.

The analysis used:

- **Chi-square tests of independence** for categorical variables
- **Mann-Whitney U tests** for continuous numerical variables
- **Cramér's V** for categorical effect size
- **Rank-biserial correlation** for numerical effect size
- **Benjamini-Hochberg False Discovery Rate (FDR) correction** for multiple testing

A significance threshold of **0.05 after FDR correction** was used.

A total of **29 variables were tested**, of which **20 remained statistically significant after FDR correction**.

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

The statistical validation provided additional support for several of the major EDA findings.

However, statistical significance indicates evidence of an association and does not establish causation.

Statistical significance and practical importance are also not identical. Some variables may be statistically significant while having relatively small effect sizes. Therefore, statistical evidence was considered alongside observed attrition rates and HR/business relevance.

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

Selected combinations of employee characteristics were statistically validated to determine whether the combined employee groups were associated with attrition.

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

The results support the observation that attrition varies substantially across employee segments defined by combinations of tenure, overtime, income, and job role.

Examples of high observed attrition segments include:

- **0–2 years + Overtime: 50.96%**
- **Q1 — Lowest Income + Overtime: 58.49%**
- **Sales Representative + Overtime: 66.67%**

These results should be interpreted as associations between combined employee characteristics and observed attrition.

The interaction validation used **combined categorical groups** and therefore does not constitute a formal regression interaction-term test.

Further multivariable analysis could investigate whether these relationships remain important when multiple employee characteristics are considered simultaneously.

---

# Attrition Rate Calculation

Attrition rates were calculated as the percentage of employees within each group who had an `Attrition` value of `"Yes"`.

The general calculation used was:

**Attrition Rate = Employees Who Left ÷ Total Employees in Group × 100**

For example:

If a group contains 100 employees and 20 employees have an Attrition value of `"Yes"`:

**Attrition Rate = 20 ÷ 100 × 100 = 20%**

This approach allows attrition to be compared fairly across employee groups of different sizes.

---

# Tableau Dashboard & Visualization

The analytical findings were presented through an interactive Tableau Public dashboard.

The dashboard contains two main analytical views.

## Dashboard 1 — HR Employee Attrition Dashboard

The main dashboard provides:

### KPI Cards

- Total Employees: **1,470**
- Employees Who Left: **237**
- Employees Who Stayed: **1,233**
- Overall Attrition Rate: **16.12%**

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

These filters allow users to examine attrition patterns across different employee segments.

## Dashboard 2 — Attrition Risk & Interaction Analysis

The second dashboard focuses on combined employee segments.

It includes:

- Years at Company × Overtime
- Income Group × Overtime
- Job Role × Overtime

This dashboard allows users to explore how observed attrition varies when multiple employee characteristics are considered together.

The Tableau dashboard complements the Python analysis by providing an interactive visual interface for exploring the findings.

---

# Analytical Limitations

The findings from this analysis should be interpreted within the limitations of the available dataset and analytical approach.

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

These segments should be interpreted as potential signals requiring further investigation rather than definitive conclusions.

## 4. Interaction Analysis and Statistical Validation

The interaction analysis and statistical validation identify associations between employee characteristics and observed attrition, but they do not establish causal relationships.

The interaction validation tested combined employee groups using categorical association tests.

It did not estimate formal regression interaction terms or establish whether the observed relationships remain independent after simultaneously controlling for other employee characteristics.

The findings should therefore be interpreted as evidence of association and as areas for further HR investigation.

## 5. Historical Dataset

The analysis reflects the employee population represented in the dataset and may not necessarily represent the current workforce or another organization.

---

# Conclusion

This project analyzed employee attrition across demographic, job-related, compensation, satisfaction, work-life, and organizational factors.

The overall observed attrition rate was **16.12%**, with 237 of the 1,470 employees represented in the dataset having left the organization.

The analysis identified several important attrition patterns. Overtime, early tenure, lower income, specific job roles, frequent business travel, and certain employee benefit levels were associated with higher observed attrition.

Statistical validation provided additional evidence for several of these relationships. Out of **29 variables tested, 20 remained statistically significant after FDR correction**, with TotalWorkingYears, MonthlyIncome, and YearsAtCompany among the variables showing the largest effect sizes.

Interaction statistical validation further supported the presence of meaningful differences across combined employee segments.

In particular:

- Employees in the lowest income group who worked overtime had an observed attrition rate of **58.49%**.
- Employees with 0–2 years at the company who worked overtime had an observed attrition rate of **50.96%**.
- Sales Representatives who worked overtime had an observed attrition rate of **66.67%**, although this segment contains a relatively small number of employees.

These findings suggest that employee attrition should be investigated using targeted strategies rather than relying only on an organization-wide view.

Potential areas for HR investigation include workload management, early-tenure support, compensation and workload review, role-specific retention efforts, and support for frequently travelling employees.

The Tableau dashboard provides an interactive way to explore the major attrition patterns, while the supporting Python analysis provides the underlying analytical evidence.

Overall, the project demonstrates how HR data can be transformed from raw employee records into **data-driven business insights and actionable retention recommendations**.

---

# Project Outcome

The completed project delivers:

- A cleaned and validated HR dataset
- A documented data dictionary
- Engineered analytical features
- Comprehensive exploratory data analysis
- Interaction analysis of selected risk factors
- Statistical validation of individual employee factors
- Statistical validation of selected interaction groupings
- Documented EDA findings
- Business insights and HR recommendations
- An interactive Tableau dashboard
- A published Tableau Public visualization
- A structured project report

The project provides a foundation for further HR analytics work, including:

- Predictive attrition modeling
- Employee risk scoring
- Formal multivariable interaction modeling
- Deeper investigation of the underlying causes of employee turnover