import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load CSV
csv_path = "/Users/yashdalvi/serious project/customer_shopping_behavior_cleaned.csv"

df = pd.read_csv(csv_path)

print(df.shape)
print(df.head())

# MySQL credentials
username = "root"
raw_password = "root@123"          # original password
password = quote_plus(raw_password)  # ENCODE it
host = "localhost"
port = "3306"
database = "customer_behavior"

# Create engine (CORRECT FORMAT)
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

table_name = "customer"

df.to_sql(
    table_name,
    engine,
    if_exists="replace",   # replaces table if exists
    index=False
)


# # Read back sample
check_df = pd.read_sql(
    "SELECT COUNT(*) AS total_rows FROM customer;",
    engine
)

print(check_df)
