
import pandas as pd

# Location of our dataset
file_path = "data/credit_card_default.csv"

# Read CSV file
df = pd.read_csv(file_path)

# Display first five records
print("\nFirst 5 Records:")
print(df.head())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display dataset information
print("\nDataset Information:")
df.info()


# Analyse the target variable
target = "default.payment.next.month"

print("\nDefault Payment Distribution:")
print(df[target].value_counts())

print("\nDefault Payment Percentage:")
print(df[target].value_counts(normalize=True) * 100)

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check data types
print("\nColumn Data Types:")
print(df.dtypes)



# -------------------------------
# DATA QUALITY CHECKS
# -------------------------------

print("\n--- DATA QUALITY CHECKS ---")

# 1. Check duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# 2. Check duplicate customer IDs
print("Duplicate customer IDs:", df["ID"].duplicated().sum())

# 3. Check unique values in categorical columns
categorical_columns = [
    "SEX",
    "EDUCATION",
    "MARRIAGE",
    "default.payment.next.month"
]

for column in categorical_columns:
    print(f"\nUnique values in {column}:")
    print(sorted(df[column].unique()))

# 4. Check age range
print("\nMinimum age:", df["AGE"].min())
print("Maximum age:", df["AGE"].max())

# 5. Check credit limit range
print("\nMinimum credit limit:", df["LIMIT_BAL"].min())
print("Maximum credit limit:", df["LIMIT_BAL"].max())
