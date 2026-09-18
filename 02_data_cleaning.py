import pandas as pd

# Load the original dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Remove columns with no analytical value
columns_to_remove = [
    "EmployeeCount",
    "Over18",
    "StandardHours",
    "EmployeeNumber"
]
df_clean = df.drop(columns=columns_to_remove)

print("Original shape:", df.shape)
print("Cleaned shape:", df_clean.shape)

print("\nRemoved columns:")
print(columns_to_remove)

# Save the cleaned dataset
df_clean.to_csv("HR_Employee_Attrition_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")