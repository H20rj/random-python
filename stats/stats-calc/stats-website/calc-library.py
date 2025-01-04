from statistics import mode, StatisticsError
from os.path import exists
from math import sqrt, erf
# Exit codes Guide:
# 0 -- Successful
# 1 -- ValueError or FileNotFoundError
# 2 -- stats.txt file created
# 3 -- stats.txt file reset

#     42, 17, 93, 56, 31, 84, 62, 19, 75, 40, 103, 28, 66, 51, 97, 13, 36, 88, 22, 69, 62
def mean(nums: list[int]) -> float:
    """
        Description:
        ___________
        Gives the mean of a list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the mean

        Returns:
        ________
        float
            The float point value of the mean
    """
    avg: float = sum(nums) / len(nums)
    return avg

def standard_dev(nums: list[int]) -> float:
    """
        Description:
        ___________
        Calculates the standard deviation of a list

        sigma = sqrt((sum(X - mu)^2) / N)

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the Standard deviation

        Returns:
        ________
        float
            The float point value of the SD
    """
    n = len(nums)
    variance = sum((X - mean(nums)) ** 2 for X in nums) / n
    return sqrt(variance)

def range_list(nums: list[int]) -> int: # range = max - min
    """
        Description:
        ___________
        Gives the range of a list of integers
        Max - Min = Range

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the range

        Returns:
        ________
        int
            The range of the list (max - min)
    """
    return maximum(nums) - minimum(nums)


def minimum(nums: list[int]) -> int:
    """
        Description:
        ____________
        Calculates the minimum value in a given list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the minimum

        Returns:
        ________
        int
            The minimum value in the given list
    """
    return sorted(nums)[0]


def maximum(nums: list[int]) -> int:
    """
        Description:
        ____________
        Calculates the maximum value in a given list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the maximum

        Returns:
        ________
        int
            The maximum value in the given list
    """
    n = len(nums) - 1
    return sorted(nums)[n]


def mode_list(nums: list[int]) -> int or str:
    """
        Description:
        ____________
        Calculates the mode of a given list of integers using statistics module

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the mode

        Returns:
        ________
        int
            The mode value of the given list
        str
            If there is no unique mode, a string is returned:
                'No unique mode'

        Raises:
        _______
        StatisticsError
            If there is no unique mode
    """
    try:
        return mode(nums)
    except StatisticsError:
        return 'No unique mode'



def quartile1(nums: list[int]) -> float:
    """
        Description:
        ____________
        Calculates Quartile 1 of a given list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate Quartile 1

        Returns:
        ________
        float
            The float point value of quartile 1
    """
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    lower_half = sorted_nums[:n//2]
    return median(lower_half)

def quartile3(nums: list[int]) -> float:
    """
        Description:
        ____________
        Calculates Quartile 3 of a given list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate Quartile 3

        Returns:
        ________
        float
            The float point value of quartile 3
    """
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 0:
        upper_half = sorted_nums[n//2:]
    else:
        upper_half = sorted_nums[n//2 + 1:]
    return median(upper_half)

def median(nums: list[int]) -> float:
    """
        Description:
        ____________
        Calculates the median of a given list of integers

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the median

        Returns:
        ________
        float
            The float point value of the median
    """
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2


def outliers(nums: list[int]) -> list[int] or str:
    """
        Description:
        ____________
        Calculates any outliers using the 1.5 times IQR rule.

        Parameters:
        ___________
        nums: list[int]
            A list of integers from which to calculate the outliers

        Returns:
        ________
        list[int]
            The list integer values of the outliers
        str
            if there are no outliers found, returns 'None'
    """


    q1 = quartile1(nums)
    q3 = quartile3(nums)
    iqr = q3 - q1


    outliers_list = [num for num in nums if num > (q3 + 1.5 * iqr) or num < (q1 - 1.5 * iqr)]
    if not outliers_list:
        return 'None'

    return outliers_list

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    z = z_score(x, mu, sigma)
    cdf: float = 0.5 * (1 + erf(z / sqrt(2)))
    return cdf


def z_score(x: float, mu: float = 0, sigma: float = 1):
    z: float = (x - mu) / sigma
    return z


def init_file() -> None:
    """
        Description:
        ____________
        Creates a stats.txt file for inputting data, and also for outputting data.

        Notes:
        ______
        Contains exit code 2, meaning a file was created
    """
    if not exists('stats.txt'):
        with open('stats.txt', 'w') as f:
            f.write("Input list of numbers seperated by a comma cuh(a, b, c, d,...) below, and then run statsCalc.py:\n\n"
                    "Then, the statistics will be output below:\n")
        print("A 'stats.txt' file was just created. Please open it, and follow the instructions there.")
        exit(2)


def read_file() -> list[int]:
    """
        Description:
        ____________
        Reads and parses stats.txt to return a list of integers used in the calculator
        Also, when the calc has been run, this function resets stats.txt for reuse, after the statsCalc.py file is rerun.

        Returns:
        ________
        list[int]
            After parsing and reading the stats.txt file, returns a list[int] to be used

        Raises:
        _______
        ValueError
             'No Input data'
                  raised when there is no input in line 2 of stats.txt
             'No valid numbers found'
                  if there are no numbers in the user input in stats.txt
        FileNotFoundError
            If no file was ever created

        Notes:
        ______
        Contains exit code 1, meaning a file error occurred
        Contains exit code 3, meaning the file stats.txt was reset for reuse

    """
    try:
        with open('stats.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) < 2:
                raise ValueError("Not enough lines in file. Be sure to input your data in the second line.\n\n    "
                                 "When in doubt, delete stats.txt and rerun statsCalc.py\n")
            if len(lines) > 5:
                with open('stats.txt', 'w') as reset:
                    reset.write(
                        "Input list of numbers seperated by a comma (a, b, c, d,...) below, and then run statsCalc.py:\n\n"
                        "Then, the statistics will be output below:\n")
                    reset.flush()
                    print("'stats.txt' file reset. File ready for reuse.")
                    exit(3)

            raw_input = lines[1].strip()
            if not raw_input:
                raise ValueError("No input data")

            numbers: list[int] = [int(num.strip()) for num in raw_input.split(",")]

            if not numbers:
                raise ValueError("No valid numbers found")
            print("File read successfully, outputting statistics.")
            return numbers
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading file: {e}")
        print("Please enter your data as a comma seperated list into the second line of the 'stats.txt' file.")
        exit(1)


def append_file(output: str) -> None:
    """
        Description:
        ____________
        Once the file is run after data is input, this function appends the output to the file.
    """
    with open('stats.txt', 'a') as f:
        f.write(f"{output}\n\nRerun statsCalc.py to reset the input file.")


def main() -> None:
    """
    Main function to run the statistical calculator.

    Initializes the file, reads input, calculates statistics,
    and appends the results to the stats.txt file.
    """
    init_file()
    nums = read_file()
    output = (
        f"\nMean: {round(mean(nums), 2)} "
        f"\nSD: {round(standard_dev(nums), 3)}"
        f"\nMinimum: {minimum(nums)}"
        f"\nQ1: {round(quartile1(nums))}"
        f"\nMedian: {round(median(nums), 2)}"
        f"\nQ3: {round(quartile3(nums))}"
        f"\nMaximum: {maximum(nums)}"
        f"\nIQR: {round(quartile3(nums)) - round(quartile1(nums))}"
        f"\nMode: {mode(nums)}"
        f"\nRange: {range_list(nums)}"
        f"\nSum: {sum(nums)}"
        f"\nOutliers: {outliers(nums)}"
    )
    append_file(output)


# def get_numbers() -> list[int]:  #get_numbers function to create a list[int] from a string like "1,2,3,4"
#     while True:
#         user_input: str = input("Input list of numbers seperated by a comma (a, b, c, d,...): \n").strip() # get unedited list and strip
#         try:
#             numbers: list[int] = [int(num.strip()) for num in user_input.split(",")]  # make sure commas are used and each value is an integer
#             return numbers
#         except ValueError:
#             print("Invalid input. Please enter a comma-separated list of integers.")


