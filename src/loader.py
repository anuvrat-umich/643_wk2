"""
This module provides functions to load CSV files into pandas DataFrames.

Functions:
- load_csv_file(file_path, pickle_path): Loads a CSV file into a pandas DataFrame 
    and optionally saves it as a pickle file.

Usage:
1. Import the module:

2. Load a CSV file:
        df = loader.load_csv_file(file_path, pickle_path)

Parameters:
- file_path (str): The path to the CSV file.
- pickle_path (str, optional): The path to save the pickle file. Default is None.

Returns:
- pd.DataFrame: The loaded data as a pandas DataFrame.

Example:
        python loader.py data/SDOH_Measures_for_ZCTA__ACS_2017-2021_20240121.csv data/df_sdoh.pkl

Author: Anuvrat Chaturvedi
Date: 2024-03-17
"""

# Import packages
import pandas as pd


def load_csv_file(file_path: str, pickle_path: str = "None") -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame and optionally saves it as a pickle file.

    Parameters:
    - file_path (str): The path to the CSV file.
    - pickle_path (str, optional): The path to save the pickle file. Default is None.

    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    print("\nData loaded successfully\n")

    if pickle_path != "None":
        data.to_pickle(pickle_path)
        print("\nData saved as pickle file\n")
    return data


# Add the following code to the bottom of the module to allow running it from the command line:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sdoh_file", help="CSV file path for Social Determinants of Health"
    )
    parser.add_argument(
        "sdoh_pickle_path",
        help="Path where output Pickle file for SDOH should be stored",
        nargs="?",
    )

    args = parser.parse_args()

    # Load the DataFrame from the CSV file and optionally save it as a pickle file
    if args.sdoh_pickle_path is None:
        df_sdoh = load_csv_file(file_path=args.sdoh_file)
    else:
        df_sdoh = load_csv_file(
            file_path=args.sdoh_file, pickle_path=args.sdoh_pickle_path
        )

    print("\nSample records for Social Determinants of Health:\n")
    print(df_sdoh.head())
