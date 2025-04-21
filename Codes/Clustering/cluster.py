import pandas as pd

#The same code is used to cluster all the datasets

# Only essential columns kept for each row
clustered_rows_1 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Area', 'Power','Cost function']

for i in range(1,101):
    filename = "./dataset/Ankle boot/Ankle boot_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_1.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_1)
    selected_df.to_csv('./clustered_data_ap_3500/Ankle boot.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Ankle boot.csv'.")

clustered_rows_2 = []

for i in range(1,101):
    filename = "./dataset/Bag/Bag_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_2.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_2)
    selected_df.to_csv('./clustered_data_ap_3500/Bag.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Bag.csv'.")

clustered_rows_3 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Coat/Coat_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_3.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_3)
    selected_df.to_csv('./clustered_data_ap_3500/Coat.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Coat.csv'.")

clustered_rows_4 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Dress/Dress_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_4.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_4)
    selected_df.to_csv('./clustered_data_ap_3500/Dress.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Dress.csv'.")

clustered_rows_5 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Pullover/Pullover_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_5.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_5)
    selected_df.to_csv('./clustered_data_ap_3500/Pullover.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Pullover.csv'.")

clustered_rows_6 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Sandal/Sandal_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_6.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_6)
    selected_df.to_csv('./clustered_data_ap_3500/Sandal.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Sandal.csv'.")

clustered_rows_7 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Shirt/Shirt_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_7.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_7)
    selected_df.to_csv('./clustered_data_ap_3500/Shirt.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Shirt.csv'.")

clustered_rows_8 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Sneaker/Sneaker_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_8.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_8)
    selected_df.to_csv('./clustered_data_ap_3500/Sneaker.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Sneaker.csv'.")

clustered_rows_9 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/Trouser/Trouser_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_9.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_9)
    selected_df.to_csv('./clustered_data_ap_3500/Trouser.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'Trouser.csv'.")

clustered_rows_10 = []
columns_to_keep = ['Multiplier', 'SSIM', 'Cost function']

for i in range(1,101):
    filename = "./dataset/T-shirt_top/T-shirt_top_"+str(i)+".csv"
    df = pd.read_csv(filename)
    df_sorted = df.sort_values(by='SSIM', ascending=False)

    for i in range(0, len(df_sorted), 3500):
        chunk = df_sorted.iloc[i:i+3500]
        min_cost_row = chunk.loc[chunk['Cost function'].idxmin()]
        clustered_rows_10.append(min_cost_row)

    selected_df = pd.DataFrame(clustered_rows_10)
    selected_df.to_csv('./clustered_data_ap_3500/T-shirt_top.csv', index=False)

print("Operation completed successfully. The selected rows have been written to 'T-shirt_top.csv'.")
