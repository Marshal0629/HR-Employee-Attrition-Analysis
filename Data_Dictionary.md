# Data Dictionary

## Overview

The HR Employee Attrition dataset contains employee-level information used to analyze factors associated with employee attrition.

The dataset originally contained 1,470 employee records and 35 columns. During data cleaning, four unnecessary columns were removed, resulting in a cleaned dataset containing 1,470 records and 31 columns.

## Column Descriptions

| Column | Description | Data Type | Analytical Role |
|---|---|---|---|
| Attrition | Indicates whether the employee left the organization | Categorical | Target variable |
| Age | Age of the employee | Numerical | Analysis |
| BusinessTravel | Frequency of business travel | Categorical | Analysis |
| DailyRate | Daily pay rate | Numerical | Analysis |
| Department | Department in which the employee works | Categorical | Analysis |
| DistanceFromHome | Distance between employee's home and workplace | Numerical | Analysis |
| Education | Education level of the employee | Ordinal | Analysis |
| EducationField | Field of education | Categorical | Analysis |
| EmployeeCount | Constant employee count field | Numerical | Removed during cleaning |
| EmployeeNumber | Unique employee identifier | Numerical/Identifier | Removed during cleaning |
| EnvironmentSatisfaction | Employee's satisfaction with the work environment | Ordinal | Analysis |
| Gender | Employee gender | Categorical | Analysis |
| HourlyRate | Hourly pay rate | Numerical | Analysis |
| JobInvolvement | Level of employee involvement in the job | Ordinal | Analysis |
| JobLevel | Employee's job level | Ordinal | Analysis |
| JobRole | Employee's job role | Categorical | Analysis |
| JobSatisfaction | Employee's job satisfaction level | Ordinal | Analysis |
| MaritalStatus | Marital status of the employee | Categorical | Analysis |
| MonthlyIncome | Monthly income of the employee | Numerical | Analysis |
| MonthlyRate | Monthly rate | Numerical | Analysis |
| NumCompaniesWorked | Number of companies the employee has previously worked for | Numerical | Analysis |
| Over18 | Indicates whether employee is over 18 | Categorical | Removed during cleaning |
| OverTime | Indicates whether the employee works overtime | Categorical | Analysis |
| PercentSalaryHike | Percentage increase in salary | Numerical | Analysis |
| PerformanceRating | Employee performance rating | Ordinal | Analysis |
| RelationshipSatisfaction | Employee's relationship satisfaction level | Ordinal | Analysis |
| StandardHours | Standard working hours | Numerical | Removed during cleaning |
| StockOptionLevel | Employee stock option level | Ordinal | Analysis |
| TotalWorkingYears | Total number of years of work experience | Numerical | Analysis |
| TrainingTimesLastYear | Number of training sessions attended in the previous year | Numerical | Analysis |
| WorkLifeBalance | Employee's work-life balance level | Ordinal | Analysis |
| YearsAtCompany | Number of years the employee has worked at the company | Numerical | Analysis |
| YearsInCurrentRole | Number of years the employee has been in the current role | Numerical | Analysis |
| YearsSinceLastPromotion | Number of years since the employee's last promotion | Numerical | Analysis |
| YearsWithCurrManager | Number of years working with the current manager | Numerical | Analysis |

## Data Type Categories

### Numerical Variables

- Age
- DailyRate
- DistanceFromHome
- HourlyRate
- MonthlyIncome
- MonthlyRate
- NumCompaniesWorked
- PercentSalaryHike
- TotalWorkingYears
- TrainingTimesLastYear
- YearsAtCompany
- YearsInCurrentRole
- YearsSinceLastPromotion
- YearsWithCurrManager

### Categorical Variables

- Attrition
- BusinessTravel
- Department
- EducationField
- Gender
- JobRole
- MaritalStatus
- OverTime

### Ordinal Variables

- Education
- EnvironmentSatisfaction
- JobInvolvement
- JobLevel
- JobSatisfaction
- PerformanceRating
- RelationshipSatisfaction
- StockOptionLevel
- WorkLifeBalance

## Columns Removed During Data Cleaning

The following columns were removed because they were not useful for employee attrition analysis:

- EmployeeCount
- EmployeeNumber
- Over18
- StandardHours