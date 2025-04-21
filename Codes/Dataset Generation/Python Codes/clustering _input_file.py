# import os
# import pandas as pd

# # Define the parent directory containing all the folders
# parent_dir = '/home/iiitb-315/Documents/Rachana/ML_dataset/dataset/'

# # List to hold combined dataframes for each folder
# all_combined_dataframes = {}

# # Iterate over each folder in the parent directory
# for folder_name in os.listdir(parent_dir):
#     folder_path = os.path.join(parent_dir, folder_name)
    
#     # Check if it's a directory
#     if os.path.isdir(folder_path):
#         # List to hold dataframes for the current folder
#         dataframes = []

#         # Iterate over the range of file numbers you want to process
#         for i in range(1, 101):  # Adjust range as needed
#             file_name = f'{folder_name}_{i}.csv'
#             file_path = os.path.join(folder_path, file_name)
            
#             # Check if the file exists
#             if os.path.isfile(file_path):
#                 # Read the CSV file
#                 df = pd.read_csv(file_path)
#                 # Append dataframe to list
#                 dataframes.append(df)
#             else:
#                 print(f"File {file_path} not found.")

#         # Concatenate all dataframes for the current folder into one
#         if dataframes:
#             combined_df = pd.concat(dataframes, ignore_index=True)
#             # Store the combined dataframe in a dictionary with the folder name as the key
#             all_combined_dataframes[folder_name] = combined_df
#         else:
#             print(f"No valid CSV files found in folder {folder_name}.")

# # Save combined dataframes for each folder to separate CSV files
# for folder_name, combined_df in all_combined_dataframes.items():
#     combined_df.to_csv(f'{folder_name}_combined.csv', index=False)
#     print(f"Saved combined data for folder {folder_name} to {folder_name}_combined.csv")

import os
import pandas as pd

# Define the directory containing the combined CSV files
combined_dir = '/home/iiitb-315/Documents/Rachana/ML_dataset/combined_files'

# List to hold dataframes from combined files
all_combined_dataframes = []

# Iterate over each file in the combined directory
for file_name in os.listdir(combined_dir):
    if file_name.endswith('_combined.csv'):
        file_path = os.path.join(combined_dir, file_name)
        # Read the combined CSV file
        df = pd.read_csv(file_path)
        # Append dataframe to the list
        all_combined_dataframes.append(df)
    else:
        print(f"File {file_name} is not a combined CSV file.")

# Concatenate all dataframes into one large dataframe
final_combined_df = pd.concat(all_combined_dataframes, ignore_index=True)

# Write the final combined dataframe to a new CSV file
final_combined_df.to_csv('/home/iiitb-315/Documents/Rachana/ML_dataset/stacked_files/combined_data.csv', index=False)
print("Saved final combined data to final_combined_data.csv")
