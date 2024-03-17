"""
This module performs data cleaning, analysis, and saving of a correlation matrix.

It imports functions from the following modules:
- `loader` for loading a CSV file
- `cleaner` for cleaning the data
- `analysis` for calculating the correlation matrix

The module expects the following command line arguments:
- `--sdoh_file`: CSV file path for Social Determinants of Health
- `--correlation_matrix_path`: Path to save the correlation matrix as a CSV file
- `--figure_path`: Path to save the histogram as a figure
- `--keep_columns`: List of columns to keep in the DataFrame
- `--rename_columns_old`: List of old column names to be renamed in the DataFrame
- `--rename_columns_new`: List of corresponding new column names after renaming
- `--index_col`: List of columns to be used as the index for the pivoted DataFrame
- `--columns_col`: List of columns to be used as the columns for the pivoted DataFrame
- `--values_col`: List of columns to be used as the values for the pivoted DataFrame
- `--plot_columns`: List of columns in the DataFrame to plot the histogram for

The module performs the following steps:
1. Parses the command line arguments
2. Loads the DataFrame from the CSV file specified by `--sdoh_file`
3. Cleans the DataFrame by keeping only the specified columns and renaming them
4. Pivots the cleaned DataFrame based on the specified index, columns, and values
5. Calculates the correlation matrix of the pivoted DataFrame
6. Saves the correlation matrix as a CSV file specified by `--correlation_matrix_path`
7. Plots a histogram of the specified columns and saves it as a figure specified by `--figure_path`

Example usage:
python main.py --sdoh_file data/SDOH_Measures_for_ZCTA__ACS_2017-2021_20240121.csv 
--correlation_matrix_path data/correlation_matrix.csv 
--figure_path data/sdoh_histogram.png 
--keep_columns "LocationName" "Measure" "Data_Value" "TotalPopulation" 
--rename_columns_old "LocationName" --rename_columns_new "ZIP" 
--index_col "ZIP" "TotalPopulation" --columns_col "Measure" --values_col "Data_Value"
--plot_columns "Crowding among housing units" "Persons of racial or ethnic minority status" 
        "Single-parent households"

Author: Anuvrat Chaturvedi
Date: 2024-03-17
"""

# Import packages
from loader import load_csv_file
from cleaner import keep_columns, rename_columns, pivot
from analysis import correlation_matrix
from visualization import plot_histogram

# Main functionality: Perform data cleaning, analysis, and saving of a correlation matrix
# It can be run from the command line
if __name__ == "__main__":
    import argparse

    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments to the parser
    parser.add_argument(
        "--sdoh_file", help="CSV file path for Social Determinants of Health"
    )
    parser.add_argument(
        "--correlation_matrix_path",
        help="Path to save the correlation matrix as a CSV file",
    )
    parser.add_argument(
        "--figure_path",
        help="Path to save the histogram as a figure",
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
    parser.add_argument(
        "--plot_columns",
        help="List of columns in the DataFrame to plot the histogram for",
        nargs="+",
    )
    # Parse the arguments
    args = parser.parse_args()

    # Load the DataFrame from the CSV file
    df_sdoh = load_csv_file(args.sdoh_file)

    # Clean the DataFrame
    df_sdoh_cleaned = keep_columns(df_sdoh, args.keep_columns)
    df_sdoh_cleaned = rename_columns(
        df_sdoh_cleaned, dict(zip(args.rename_columns_old, args.rename_columns_new))
    )
    df_sdoh_pivoted = pivot(
        df_sdoh_cleaned,
        index_col=args.index_col,
        columns_col=args.columns_col,
        values_col=args.values_col,
    )

    # Calculate the correlation matrix
    correlation_matrix_df = correlation_matrix(df_sdoh_pivoted)

    # Save the correlation matrix as a CSV file
    correlation_matrix_df.to_csv(args.correlation_matrix_path, index=False)
    print("\nCorrelation matrix saved successfully as a CSV file\n")

    # Save the histogram
    plot_histogram(
        df=df_sdoh_pivoted,
        columns=args.plot_columns,
        title=f"SDOH Histogram (N={df_sdoh_pivoted.shape[0]})",
        bins=10,
        path=args.figure_path,
    )
