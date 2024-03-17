"""
This script contains a test suite for the various functions in the project.

The script tests the following functions from different modules:
- loader: load_csv_file
- cleaner: keep_columns, rename_columns, pivot
- analysis: correlation_matrix
- visualization: plot_histogram

The test suite performs various assertions to validate the functionality of each function.

Author: Anuvrat Chaturvedi
Date: 2024-03-17
"""

# Import packages
from loader import load_csv_file
from cleaner import keep_columns, rename_columns, pivot
from analysis import correlation_matrix
from visualization import plot_histogram
import pandas as pd
import os


# Define the test suite
def test_all_functions_in_project():
    """
    Test the loader module functions.

    This function tests the following functions from the loader module:
    - load_csv_file
    - keep_columns
    - rename_columns
    - pivot
    - correlation_matrix
    - plot_histogram

    It performs various assertions to validate the functionality of each function.

    Raises:
        AssertionError: If any of the assertions fail.
    """
    # Test the load_csv_file function
    try:
        sdoh_file = "data/SDOH_Measures_for_ZCTA__ACS_2017-2021_20240121.csv"
        df = load_csv_file(sdoh_file)
    except FileNotFoundError:
        assert False, "File not found"
    except Exception as e:
        assert False, e

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (50000, 16)

    # Test the keep_columns function
    columns_to_keep = ["LocationName", "Measure", "Data_Value", "TotalPopulation"]
    df = keep_columns(df, columns_to_keep)
    assert df.shape == (50000, 4)

    # Test the rename_columns function
    old_column_names = ["LocationName"]
    new_column_names = ["ZIP"]
    df = rename_columns(df, dict(zip(old_column_names, new_column_names)))
    assert new_column_names[0] in df.columns.tolist()

    # Test the pivot function
    index_col = ["ZIP", "TotalPopulation"]
    columns_col = ["Measure"]
    values_col = ["Data_Value"]
    df = pivot(df, index_col, columns_col, values_col)
    assert df.shape == (7488, 11)

    # Test the correlation_matrix function
    assert df.corr().equals(correlation_matrix(df))

    # Test the plot_histogram function
    figure_path = "data/histogram.png"
    plot_columns = [
        "Crowding among housing units",
        "Persons of racial or ethnic minority status",
    ]
    plot_histogram(df, plot_columns, figure_path)
    assert os.path.exists(figure_path)
    os.remove(figure_path)
