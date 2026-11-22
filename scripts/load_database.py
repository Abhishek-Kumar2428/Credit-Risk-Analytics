
import pandas as pd
import sqlite3

# Read cleaned dataset
df = pd.read_csv("outputs/cleaned_credit_data.csv")

# Create SQLite database
connection = sqlite3.connect("outputs/credit_risk.db")

# Load data into SQL table
df.to_sql(
    "credit_customers",
    connection,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into SQLite!")

# Run a sample SQL query
query = """
SELECT
    COUNT(*) AS total_customers,
    ROUND(AVG(default_next_month) * 100, 2) AS default_rate
FROM credit_customers;
"""

result = pd.read_sql_query(query, connection)

print("\nCustomer Summary:")
print(result)

connection.close()
