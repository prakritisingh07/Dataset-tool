#Dataset_modifier

A simple Python-based tool for processing and analyzing CSV datasets with an interactive menu-driven interface.

## Project Information

*Created By:*
- Prakriti Singh
- Ashwani Kumari Singh

## Description

This project is a command-line data processing tool built with Python and Pandas. It allows users to load CSV files and perform various data manipulation operations through an easy-to-use menu system.

## Features

The tool provides the following functionalities:

1. *Sort Data* - Sort dataset by any column in ascending or descending order
2. *Clean Data* - Remove or fill missing values using multiple methods:
   - Drop all rows with NA values
   - Drop NA values in specific columns
   - Fill NA with custom values
   - Fill NA with column mean (for numeric data)
   - Forward fill method
3. *Filter Data* - Filter rows based on conditions:
   - Numeric columns: greater than, less than, equal to, between values
   - Text columns: contains, equals, starts with, ends with
4. *Statistics* - Display statistical summaries including:
   - Descriptive statistics for numeric columns
   - Value counts for categorical columns
   - Correlation matrix
5. *Remove Duplicates* - Eliminate duplicate rows from dataset
6. *Export Data* - Save modified dataset to CSV format
7. *View Info* - Display dataset information, column types, and missing values

## Project Structure

data_tool/
├── main.py # Main entry point and menu system
├── load.py # File loading and data info functions
└── ops/ # Operations modules
├── sort.py # Sorting operations
├── clean.py # Data cleaning operations
├── filter.py # Filtering operations
├── stats.py # Statistical analysis
└── save.py # Export operations

text

## Technologies Used

- *Python 3.x* - Programming language
- *Pandas* - Data manipulation and analysis library

## Installation

1. Make sure Python 3.x is installed on your system

2. Install required library:
pip install pandas

text

3. Download all project files and maintain the folder structure

## Usage

1. Open terminal/command prompt

2. Navigate to the project directory:
cd path/to/data_tool

text

3. Run the program:
python main.py

text

4. Enter the path to your CSV file when prompted (use forward slashes):

D:/Downloads/data.csv

text

5. Choose operations from the menu by entering numbers 1-8

6. Follow on-screen prompts for each operation

## Example Workflow

1. Load a CSV file
2. View data info (option 7)
3. Clean missing values (option 2)
4. Filter data based on conditions (option 3)
5. Sort by specific column (option 1)
6. Save modified dataset (option 6)

## File Format

- *Supported format:* CSV files only
- *Input:* Any CSV file with headers
- *Output:* CSV file (user-defined filename)

## Requirements

- Python 3.6 or higher
- Pandas library
- CSV data files

## Notes

- Use forward slashes (/) in file paths to avoid errors
- The program preserves original data until you choose to save
- All operations are performed on the currently loaded dataset
- Statistics work best with clean data (minimal missing values)
