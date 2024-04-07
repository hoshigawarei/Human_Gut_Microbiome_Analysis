# MSM
query_bacterium_name_at_row requires .xlsx file format: bacteria names are listed starting from the second row, and the name of the bacteria is in the first column.
query_bacterium_name_at_row:
    Function to read an Excel file and query bacterium names at specific rows.

    Reads the Excel file specified by the user.
    Prompts the user to input the row number of the bacterium to be queried.
    Outputs the content of the first column corresponding to the specified row number.

classify_data classifies the excel table that stores the overall data according to the information in the txt file.
classify_data(excel_file_path):
    Classify data from an Excel file based on keywords provided in a text file.

    Args:
        excel_file_path (str): Path to the Excel file to be classified.

    Returns:
        pandas.DataFrame: DataFrame containing the classified data.

save_to_excel stores the classified information in classify into a new excel table
save_to_excel(dataframe, output_file_path):
    Save DataFrame to an Excel file.

    Args:
        dataframe (pandas.DataFrame): DataFrame to be saved.
        output_file_path (str): Path to save the Excel file.

plot_excel_data performs data analysis on the classified excel tables and draws visual charts. The specific data results will be stored in mat_output.txt in the same directory.。
plot_excel_data(file_path):
    Plot data from an Excel file.

    Parameters:
    - file_path (str): Path to the Excel file or 'AM' to plot area numbers.

    If file_path is 'AM', it plots area numbers. Otherwise, it analyzes the data
    from the Excel file and plots accordingly.

    
