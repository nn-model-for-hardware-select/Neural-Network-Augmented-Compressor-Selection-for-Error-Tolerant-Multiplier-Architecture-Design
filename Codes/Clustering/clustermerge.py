import pandas as pd
import glob

# List all CSV files in the directory (adjust the pattern if needed)
file_pattern = './clustered_data_ap_3500/*.csv'  # Replace with the actual path and pattern to match your CSV files
csv_files = glob.glob(file_pattern)
columns_to_keep = ['Multiplier', 'SSIM', 'Area', 'Power', 'Cost function']




# List to store DataFrames
df_list = []

# Read each CSV file and append to the list
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Concatenate all DataFrames
combined_df = pd.concat(df_list, ignore_index=True)
# Select only the desired columns
selected_columns = combined_df[columns_to_keep]

# Write the concatenated DataFrame to a new CSV file
selected_columns.to_csv('./stacked_files/combined_file_ap_3500.csv', index=False)

print("All CSV files have been combined into 'combined_file_ap_3500.csv'.")