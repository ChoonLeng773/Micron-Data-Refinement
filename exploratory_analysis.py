import pandas as pd
import matplotlib.pyplot as plt

# Read the Parquet file
df = pd.read_parquet("train/incoming_run_data_1.parquet", engine="pyarrow")

print("Data from Parquet file:")
print(df.columns)
print(df.describe())


# Describe and transpose for better plotting
desc = df.describe().transpose()

# Plotting the describe statistics
desc[["mean", "std", "min", "max"]].plot(kind="bar", figsize=(12, 6))

plt.title("Descriptive Statistics")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
