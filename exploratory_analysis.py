import pandas as pd

# Read the Parquet file
df = pd.read_parquet("train/incoming_run_data_1.parquet", engine="pyarrow")

print("Data from Parquet file:")
print(df.columns)
print(df.describe())
