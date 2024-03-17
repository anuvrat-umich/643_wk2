# SIADS 643 wk2 Code Crafting - Anuvrat Chaturvedi - March 17th, 2024

## Project Description

This project aims to create a correlation matrix and histograms for the given data. The code provided in this repository allows you to perform the following tasks:

- Load the data
- Calculate the correlation matrix
- Generate histograms for the variables

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the code to generate the correlation matrix and histograms.

## Usage

To use the code, follow these steps:

1. Open the code file in your preferred programming environment.
2. Modify the file path or data source if necessary.
3. Run the code to generate the desired output.

## Dependencies

This project has the following dependencies:

- Python 3.7 or higher
- Pandas library
- Matplotlib library
- Pytest library

Make sure you have these dependencies installed before running the code. Install using `pip install -r 643_wk2/src/requirements.txt`

## Sample code to execute

Run the following code in the in your preferred Python programming environment with installed dependencies. It should be run as a single line argument.

python main.py --sdoh_file data/SDOH_Measures_for_ZCTA\_\_ACS_2017-2021_20240121.csv --correlation_matrix_path data/correlation_matrix.csv --figure_path data/sdoh_histogram.png --keep_columns "LocationName" "Measure" "Data_Value" "TotalPopulation" --rename_columns_old "LocationName" --rename_columns_new "ZIP" --index_col "ZIP" "TotalPopulation" --columns_col "Measure" --values_col "Data_Value" --plot_columns "Crowding among housing units" "Persons of racial or ethnic minority status" "Single-parent households"

## Unit Testing

To run the unit tests for this project, execute the `test_all.py` script. This script contains a comprehensive set of tests to ensure the functionality of the code.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](https://github.com/anuvrat-umich/643_wk2/blob/main/LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact the project owner, Anuvrat Chaturvedi, at [anuvrat@umich.edu](mailto:anuvrat@umich.edu).
