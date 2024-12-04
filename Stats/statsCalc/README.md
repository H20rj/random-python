Statistical Calculator
======================

This is a Python-based statistical calculator that reads input data from a `stats.txt` file, performs various statistical calculations, and appends the results back to the same file.

Features
--------

-   Calculates:
    -   Mean
    -   Standard Deviation
    -   Minimum and Maximum
    -   Quartiles (Q1, Median, Q3)
    -   Interquartile Range (IQR)
    -   Mode
    -   Range
    -   Sum
    -   Outliers using the 1.5 × IQR rule
-   Automatically handles the creation and resetting of the `stats.txt` file

Getting Started
---------------

### Prerequisites

-   Python 3.x installed on your system

### Installation

1.  **Clone the repository:**

        https://github.com/H20rj/Game-Design-Python.git

2.  **Navigate to the project directory**



Usage
-----

1.  **Run the main script:**

    bash

    Copy code

    `python statsCalc.py`

2.  **Input your data:**

    -   If it's the first time running the script, a `stats.txt` file will be created.

    -   Open `stats.txt` and follow the instructions:

        -   Enter your list of numbers separated by commas on the second line.

        Example:
    

        Input list of numbers separated by a comma (a, b, c, d,...) below, and then run statsCalc.py:

        42, 17, 93, 56, 31, 84, 62, 19, 75, 40, 103, 28, 66, 51, 97, 13, 36, 88, 22, 69, 62

        Then, the statistics will be output below:

3.  **Run the script again to perform calculations:**


    python statsCalc.py

4.  **View the results:**

    -   The statistical results will be appended to the `stats.txt` file below your input data.

        Example output:
    

        Mean: 55.24
        SD: 27.436
        Minimum: 13
        Q1: 31
        Median: 56
        Q3: 75
        Maximum: 103
        IQR: 44
        Mode: 62
        Range: 90
        Sum: 1158
        Outliers: [103]

        Rerun statsCalc.py to reset the input file.

5.  **Reset for new calculations:**

    -   To perform calculations on a new set of data, rerun `statsCalc.py`, and the `stats.txt` file will be reset for new input.

Exit Codes
----------

The script uses exit codes to indicate the status of execution:

-   **0** --- Successful execution
-   **1** --- ValueError or FileNotFoundError (e.g., missing input data or file)
-   **2** --- `stats.txt` file created
-   **3** --- `stats.txt` file reset

Function Overview
-----------------

The `calcLibrary.py` contains the following functions:

-   **`mean(nums: list[int]) -> float`**: Calculates the mean of the list.
-   **`standard_dev(nums: list[int]) -> float`**: Calculates the standard deviation.
-   **`minimum(nums: list[int]) -> int`**: Finds the minimum value.
-   **`maximum(nums: list[int]) -> int`**: Finds the maximum value.
-   **`median(nums: list[int]) -> float`**: Calculates the median.
-   **`quartile1(nums: list[int]) -> float`**: Calculates the first quartile (Q1).
-   **`quartile3(nums: list[int]) -> float`**: Calculates the third quartile (Q3).
-   **`range_list(nums: list[int]) -> int`**: Calculates the range (Max - Min).
-   **`mode_list(nums: list[int]) -> int or str`**: Calculates the mode; returns `'No unique mode'` if there isn't one.
-   **`outliers(nums: list[int]) -> list[int] or str`**: Identifies outliers using the 1.5 × IQR rule; returns `'None'` if there are no outliers.
-   **`init_file() -> None`**: Initializes the `stats.txt` file.
-   **`read_file() -> list[int]`**: Reads and parses input from `stats.txt`.
-   **`append_file(output: str) -> None`**: Appends the output to `stats.txt`.
-   **`main() -> None`**: Main function to run the statistical calculator.

Notes
-----

-   The script automatically creates and manages the `stats.txt` file.
-   Ensure your data is correctly formatted as a comma-separated list of integers.
-   The script handles exceptions and provides meaningful error messages.

