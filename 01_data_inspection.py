import utils.session
import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("Rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nUnique values in each column:")
print(df.nunique().sort_values())

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())
    
print("\nNumerical columns summary:")
print(df.describe().T)

print("\nLogical consistency checks:")

print(
    "YearsAtCompany > TotalWorkingYears:",
    (df["YearsAtCompany"] > df["TotalWorkingYears"]).sum()
)

print(
    "YearsInCurrentRole > YearsAtCompany:",
    (df["YearsInCurrentRole"] > df["YearsAtCompany"]).sum()
)

print(
    "YearsWithCurrManager > YearsAtCompany:",
    (df["YearsWithCurrManager"] > df["YearsAtCompany"]).sum()
)

print(
    "YearsSinceLastPromotion > YearsAtCompany:",
    (df["YearsSinceLastPromotion"] > df["YearsAtCompany"]).sum()
)

numerical_columns = df.select_dtypes(include="number").columns

for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = ((df[column] < lower_bound) | (df[column] > upper_bound)).sum()

    print(f"{column}: {outliers} potential outliers")

coded_columns = [
    "Education",
    "EnvironmentSatisfaction",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "WorkLifeBalance"
]

print("\nCoded categorical variables:")

for column in coded_columns:
    print(f"\n{column}:")
    print(df[column].value_counts().sort_index())