from flask import Flask, render_template, request
from calcLibrary import *

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    input_data = request.form['numbers']
    try:
        # Validate and parse the input
        if input_data.strip().isdigit():  # Check if the input is a single number
            nums = [int(input_data.strip())]
        else:
            nums = [int(x.strip()) for x in input_data.split(',') if x.strip().isdigit()]

        # Check if nums is not empty after parsing
        if not nums:
            raise ValueError("Input does not contain valid numbers.")

        # Calculate statistics
        stats = {
            "Mean": round(mean(nums), 2),
            "Standard Deviation": round(standard_dev(nums), 2),
            "Minimum": minimum(nums),
            "Maximum": maximum(nums),
            "Median": median(nums),
            "Q1": quartile1(nums),
            "Q3": quartile3(nums),
            "IQR": quartile3(nums) - quartile1(nums),
            "Mode": mode_list(nums),
            "Range": range_list(nums),
            "Sum": sum(nums),
            "Outliers": outliers(nums) if outliers(nums) else "None"
        }

        return render_template('result.html', stats=stats, numbers=nums)

    except ValueError as e:
        # Render the input form with an error message
        return render_template('index.html',
                               error=f"Invalid input: {e}. Please enter a valid, comma-separated list of integers.")


if __name__ == '__main__':
    app.run(debug=True, port=5050, host = "0.0.0.0")
