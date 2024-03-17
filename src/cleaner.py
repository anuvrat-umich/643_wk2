"""
This module provides functions to clean up a DataFrame by keeping only specified columns, 
renaming columns, and pivoting the DataFrame.

Usage:
1. Import the module:
    import cleaner

2. Load a DataFrame:
    df = pd.read_pickle("path/to/data.pkl")
    
3. Keep only specified columns:
    df_keep = cleaner.keep_columns(df, cols_to_keep)
    
4. Rename columns:
    df_renamed = cleaner.rename_columns(df_keep, cols_to_rename)
    
5. Pivot the DataFrame:
    df_pivoted = cleaner.pivot(df_renamed, index_col, columns_col, values_col)
    
6. Save the cleaned and pivoted DataFrame as a pickle file, if desired:
    df_pivoted.to_pickle("path/to/output.pkl")

Or run the module from the command line:
    python cleaner.py <sdoh_file> <sdoh_edited_pickle_path> --keep_columns <cols_to_keep> 
    --rename_columns_old <old_col_names> --rename_columns_new <new_col_names> 
    --index_col <index_col> --columns_col <columns_col> --values_col <values_col>

Example:
    python cleaner.py data/df_sdoh.pkl data/df_sdoh_pivoted.pkl 
    --keep_columns "LocationName" "Measure" "Data_Value" "TotalPopulation" 
    --rename_columns_old "LocationName" --rename_columns_new "ZIP" 
    --index_col "ZIP" "TotalPopulation" --columns_col "Measure" --values_col "Data_Value"

Author: Anuvrat Chaturvedi
Date: 2024-03-17
"""

# Import packages
import pandas as pd


# Define functions
def keep_columns(df: pd.DataFrame, cols_to_keep: list) -> pd.DataFrame:
    """
    Keep only the specified columns in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to clean.
    - cols_to_keep (list): The list of columns to keep.

    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    outdf = df[cols_to_keep]
    print("\nOnly required columns kept successfully\n")
    return outdf


def rename_columns(df: pd.DataFrame, cols_to_rename: dict) -> pd.DataFrame:
    """
    Rename the specified columns in the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to clean.
    - cols_to_rename (dict): The dictionary of columns to rename.

    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    outdf = df.rename(columns=cols_to_rename)
    print("\nColumns renamed successfully\n")
    return outdf


def pivot(
    inpdf: pd.DataFrame, index_col: list, columns_col: list, values_col: list
) -> pd.DataFrame:
    """
    Pivots a DataFrame based on the specified index, columns, and values.

    Args:
        inpdf (DataFrame): The input DataFrame to be pivoted.
        index_col (list): The column(s) to be used as the index for the pivoted DataFrame.
        columns_col (list): The column(s) to be used as the columns for the pivoted DataFrame.
        values_col (list): The column(s) to be used as the values for the pivoted DataFrame.

    Returns:
        DataFrame: The pivoted DataFrame.

    """
    # Check if the index, columns, and values are single columns. If yes, convert them to strings
    if len(index_col) == 1:
        index_col = index_col[0]
    if len(columns_col) == 1:
        columns_col = columns_col[0]
    if len(values_col) == 1:
        values_col = values_col[0]

    # Pivot the DataFrame
    outdf = (
        inpdf.pivot(index=index_col, columns=columns_col, values=values_col)
        .reset_index()
        .rename_axis(None, axis=1)
    )

    print("\nDataFrame pivoted successfully\n")
    return outdf


# Add the following code to the bottom of the module to allow running it from the command line:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sdoh_file",
        help="DataFrame pickle path for Social Determinants of Health",
    )
    parser.add_argument(
        "sdoh_edited_pickle_path",
        help="Path where output Pickle file for SDOH should be stored",
    )
    parser.add_argument(
        "--keep_columns",
        help="List of columns to keep in the DataFrame",
        nargs="+",
    )
    parser.add_argument(
        "--rename_columns_old",
        help="List of old column names to be renamed in the DataFrame",
        nargs="+",
    )
    parser.add_argument(
        "--rename_columns_new",
        help="List of corresponding new column names after renaming",
        nargs="+",
    )
    parser.add_argument(
        "--index_col",
        help="List of columns to be used as the index for the pivoted DataFrame",
        nargs="+",
    )
    parser.add_argument(
        "--columns_col",
        help="List of columns to be used as the columns for the pivoted DataFrame",
        nargs="+",
    )
    parser.add_argument(
        "--values_col",
        help="List of columns to be used as the values for the pivoted DataFrame",
        nargs="+",
    )
    args = parser.parse_args()

    # Load the DataFrame from the pickle file
    df_sdoh = pd.read_pickle(args.sdoh_file)

    # Print keep_columns values
    print("args.keep_columns: ", args.keep_columns)

    # Print rename_columns_old values
    print("args.rename_columns_old: ", args.rename_columns_old)

    # Print rename_columns_new values
    print("args.rename_columns_new: ", args.rename_columns_new)

    # Print index_col values
    print("args.index_col: ", type(args.index_col), args.index_col)

    # Print columns_col values
    print("args.columns_col: ", type(args.columns_col), list(args.columns_col))

    # Print values_col values
    print("args.values_col: ", type(args.values_col), args.values_col)

    # Apply the keep_columns function
    df_sdoh_keep = keep_columns(df=df_sdoh, cols_to_keep=list(args.keep_columns))

    # Create a dictionary of old and new column names
    args.rename_columns = dict(zip(args.rename_columns_old, args.rename_columns_new))

    # Apply the rename_columns function
    df_sdoh_renamed = rename_columns(
        df=df_sdoh_keep, cols_to_rename=args.rename_columns
    )
    # df_sdoh_edited = df_sdoh_keep

    # Transform the DataFrame by pivoting it
    df_sdoh_pivoted = pivot(
        inpdf=df_sdoh_renamed,
        index_col=args.index_col,
        columns_col=args.columns_col,
        values_col=args.values_col,
    )

    # Save the cleaned and renamed DataFrame as a pickle file
    df_sdoh_pivoted.to_pickle(args.sdoh_edited_pickle_path)

    # Print the cleaned, renamed and pivoted DataFrame
    print("Cleaned, renamed and pivoted DataFrame:")
    print(df_sdoh_pivoted.head())
