"""
This module contains functions for analyzing data and calculating correlation matrices.

Usage:
1. Import the module:
    import analysis

2. Load a DataFrame:
    df = pd.read_pickle("path/to/data.pkl")

3. Calculate the correlation matrix:
    correlation_matrix = analysis.correlation_matrix(df)

4. Save the correlation matrix as a CSV file, if desired:
    correlation_matrix.to_csv("path/to/output.csv", index=False)

Or run the module from the command line:
    python analysis.py --sdoh_pivoted_file <path_to_sdoh_file> 
    --correlation_matrix_path <path_to_save_correlation_matrix>

Example:
    python analysis.py --sdoh_pivoted_file data/df_sdoh_pivoted.pkl 
    --correlation_matrix_path data/correlation_matrix.csv

Author: Anuvrat Chaturvedi
Date: 2024-03-17
"""

# Import packages
import pandas as pd


# Define functions
def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the correlation matrix for the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame for which to calculate the correlation matrix.

    Returns:
    - pd.DataFrame: The correlation matrix.
    """
    correlation_matrix = df.corr()
    print("\nCorrelation matrix calculated successfully\n")
    return correlation_matrix


# Add the following code to the bottom of the module to allow running it from the command line:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sdoh_pivoted_file", help="Path for cleaned up SDOH pickle file"
    )
    parser.add_argument(
        "--correlation_matrix_path",
        help="Path to save the correlation matrix as a CSV file",
    )
    args = parser.parse_args()

    df_sdoh_pivoted = pd.read_pickle(args.sdoh_pivoted_file)
    correlation_matrix(df_sdoh_pivoted).to_csv(
        args.correlation_matrix_path, index=False
    )
