
import pandas as pd
import os

# Load original dataset
df = pd.read_csv("data/credit_card_default.csv")

print("Original dataset shape:", df.shape)

# Remove duplicate rows, if any
df = df.drop_duplicates()

# Standardise column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(".", "_", regex=False)
    .str.replace(" ", "_", regex=False)
)

# Rename target column for easier usage
df = df.rename(columns={
    "default_payment_next_month": "default_next_month"
})

# Create a readable default status column
df["default_status"] = df["default_next_month"].map({
    0: "No Default",
    1: "Default"
})

# Create credit limit categories
df["credit_limit_band"] = pd.cut(
    df["limit_bal"],
    bins=[0, 50000, 100000, 200000, 500000, float("inf")],
    labels=[
        "0-50K",
        "50K-100K",
        "100K-200K",
        "200K-500K",
        "500K+"
    ]
)

# Create age categories
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=[
        "Below 25",
        "25-35",
        "36-45",
        "46-55",
        "Above 55"
    ]
)

# Create output directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Export cleaned dataset
df.to_csv("outputs/cleaned_credit_data.csv", index=False)

print("\nCleaned dataset shape:", df.shape)
print("\nDefault status distribution:")
print(df["default_status"].value_counts())

print("\nCleaned dataset saved successfully!")
