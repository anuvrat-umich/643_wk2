"""
This module provides functions for visualizing data using histograms.

The main function in this module is `plot_histogram`, which plots a histogram 
of the specified columns in a DataFrame.

Usage:
1. Import the module:
    import visualization

2. Load a DataFrame:
    df = pd.read_pickle("path/to/data.pkl")

3. Specify the columns to plot:
    columns_to_plot = ["column1", "column2", "column3"]

4. Plot the histogram:
    visualization.plot_histogram(df, columns_to_plot, title="My Histogram", 
    bins=20, path="output/histogram.png")

Parameters:
- df (pd.DataFrame): The DataFrame containing the data.
- columns (list): The list of names of the columns to plot.
- title (str, optional): The title of the histogram. Default is "Histogram".
- bins (int, optional): The number of bins to use for the histogram. Default is 10.
- path (str, optional): The path to save the histogram as a figure. Default is "data/histogram.png".

Returns:
- None

Or run the module from the command line:
    python visualization.py --sdoh_pivoted_file <path_to_sdoh_file> 
    --figure_path <path_to_save_histogram> --plot_columns <columns_to_plot>

Example:
    python visualization.py --sdoh_pivoted_file data/df_sdoh_pivoted.pkl 
    --figure_path data/sdoh_histogram.png 
    --plot_columns "Crowding among housing units" "Persons of racial or ethnic minority status" 
        "Single-parent households"
    
Author: Anuvrat Chaturvedi
Date: 2024-03-17

"""

# Import packages
import pandas as pd
import matplotlib.pyplot as plt


# Define functions
def plot_histogram(
    df: pd.DataFrame,
    columns: list,
    title="Histogram",
    bins: int = 10,
    path: str = "data/histogram.png",
) -> None:
    """
    Plot a histogram of the specified columns in the DataFrame - one column per row.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - columns (list): The list of names of the columns to plot.
    - title (str, optional): The title of the histogram. Default is "Histogram".
    - bins (int, optional): The number of bins to use for the histogram. Default is 10.
    - path (str, optional): The path to save the histogram as a figure.
        Default is "data/histogram.png".

    Returns:
    - None

    Example Usage:
        import pandas as pd
        import matplotlib.pyplot as plt

        data = pd.read_csv("data.csv")
        columns_to_plot = ["column1", "column2", "column3"]
        plot_histogram(data, columns_to_plot, title="My Histogram", bins=20,
            path="output/histogram.png")
    """
    fig, axes = plt.subplots(len(columns), 1, figsize=(10, len(columns) * 2))

    for i, col in enumerate(columns):
        axes[i].hist(df[col], bins=bins)
        axes[i].set_title(col)

    fig.suptitle(title)
    plt.tight_layout()
    plt.savefig(path)
    print(f"\nHistogram saved successfully at {path}\n")


# Add the following code to the bottom of the module to allow running it from the command line:
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sdoh_pivoted_file", help="Path for cleaned up SDOH pickle file"
    )
    parser.add_argument(
        "--figure_path",
        help="Path to save the histogram as a figure",
    )
    parser.add_argument(
        "--plot_columns",
        help="List of columns in the DataFrame to plot the histogram for",
        nargs="+",
    )
    args = parser.parse_args()

    df_sdoh_pivoted = pd.read_pickle(args.sdoh_pivoted_file)

    plot_histogram(
        df=df_sdoh_pivoted,
        columns=args.plot_columns,
        title=f"SDOH Histogram (N={df_sdoh_pivoted.shape[0]})",
        bins=10,
        path=args.figure_path,
    )
