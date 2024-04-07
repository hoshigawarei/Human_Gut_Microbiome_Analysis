import pandas as pd

def query_bacterium_name_at_row():
    """
    Function to read an Excel file and query bacterium names at specific rows.

    Reads the Excel file specified by the user.
    Prompts the user to input the row number of the bacterium to be queried.
    Outputs the content of the first column corresponding to the specified row number.
    """
    # Read the Excel file
    excel_file = input("Please enter the location and name of the Excel file: ")
    try:
        data = pd.read_excel(excel_file)
    except FileNotFoundError:
        print("The specified Excel file cannot be found. Please re-enter.")
        return

    # Query loop
    while True:
        row_number = input("Please enter the row number of the bacterium to be queried (enter 'n' to exit): ")

        # Check if the user chooses to exit
        if row_number.lower() == 'n':
            print("Query exited.")
            break

        try:
            row_number = int(row_number)
            if row_number < 1 or row_number > len(data):
                print("The input row number is out of range. Please re-enter.")
                continue
        except ValueError:
            print("Please enter a valid row number or 'N' to terminate the loop.")
            continue

        # Output the content of the first column corresponding to the specified row number
        bacterium = data.iloc[row_number - 1, 0]
        print(f"The bacterium name at row {row_number} is: {bacterium}")

# Test the function
query_bacterium_name_at_row()