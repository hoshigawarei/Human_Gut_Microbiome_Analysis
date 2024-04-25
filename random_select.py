import pandas as pd
import random

# Load data from the original CSV file
csv_file = input('Please enter the address of the CSV file that needs to be processed:')
data = pd.read_csv(csv_file)
row = [int(0) for i in range(30)]
j = 0
while True:
    row[j] = int(input(f'Please enter the starting number of rows for the {j/3}th group of people to filter (Enter -1 to stop):'))
    if row[j] == -1:
        break
    row[j + 1] = int(input(f'Please enter the ending number of rows for the {j/3}th group of people to filter:'))
    row[j + 2] = int(input(f'Please enter the number n of rows to be filtered out for the {j/3}th category of people:'))
    j += 3
j -= 3
out_file = input('Please enter the path to save the sub-file:')
for i in range(10):
    new_data = pd.DataFrame()  # Create an empty DataFrame to store the new data
    k = 0
    first_row = data.iloc[0]
    while k <= j:
        random_samples = random.sample(range(row[k], row[k + 1]), row[k + 2])
        selected_rows = data.iloc[random_samples]  # Select random rows from the original data
        if k == 0:
            new_data = pd.concat([first_row.to_frame().T, selected_rows])  # Concatenate the first row and selected rows
        elif k > 0:
            new_data = pd.concat([new_data, selected_rows])  # Concatenate the new selected rows to the existing data
        k += 3
    # Save the merged data to a new CSV file
    new_data.to_csv(f"{out_file}_{i}.csv", index=False)
