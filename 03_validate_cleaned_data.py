import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("HR_Employee_Attrition_Cleaned.csv")

print("Cleaned dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nRemoved columns still present:")
removed_columns = [
    "EmployeeCount",
    "Over18",
    "StandardHours",
    "EmployeeNumber"
]

print([column for column in removed_columns if column in df.columns])
