import pandas as pd
import os
from warnings import simplefilter

def classify_data(excel_file_path):
    """
    Classify data from an Excel file based on keywords provided in a text file.

    Args:
        excel_file_path (str): Path to the Excel file to be classified.

    Returns:
        pandas.DataFrame: DataFrame containing the classified data.
    """
    simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

    try:
        data = pd.read_excel(excel_file_path)
    except FileNotFoundError:
        print("Error: The specified Excel file cannot be found.")
        return None

    txt_file_path = input("Please enter the path to the text file containing the keyword information: ")


    if not os.path.isfile(txt_file_path):
        print("Error: The specified text file cannot be found.")
        return None

    try:
        with open(txt_file_path, 'r') as file:
                keywords = [line.strip() for line in file]
    except Exception as e:
        print(f"An error occurred while reading the text file: {e}")
        return None

    # Create a new DataFrame to store the classified data
    classified_data = pd.DataFrame()

    # Search for keywords in column names and copy matching columns to the new DataFrame
    for keyword in keywords:
        for column_name in data.columns:
            if keyword.lower() in column_name.lower():
                classified_data[keyword] = data[column_name]
                break

    print("Data classification completed.")
    return classified_data

def save_to_excel(dataframe, output_file_path):
    """
    Save DataFrame to an Excel file.

    Args:
        dataframe (pandas.DataFrame): DataFrame to be saved.
        output_file_path (str): Path to save the Excel file.
    """
    dataframe.to_excel(output_file_path, index=False)
    print(f"Data has been saved to {output_file_path}")

def main():
    """
    Main function to classify data from an Excel file based on keywords provided in a text file.
    """
    excel_file_path = input("Please enter the path to the Excel file that needs to be classified: ")
    classified_data = classify_data(excel_file_path)
    if classified_data is not None:
        output_file_path = input("Please enter the path to save the classified data (including file name with .xlsx extension): ")
        save_to_excel(classified_data, output_file_path)

if __name__ == "__main__":
    main()
