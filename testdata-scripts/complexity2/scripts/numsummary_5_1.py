import numpy as np

def five_number_summary(data):
    """
    Calculate and return the five-number summary of the given data.

    Parameters:
        data (list of int/float): List of numbers to analyze.

    Returns:
        dict: Five-number summary including min, Q1, median, Q3, and max.
    """
    if not data:
        raise ValueError("Data list is empty.")
    summary = np.percentile(data, [0, 25, 50, 75, 100])
    return {
        'min': summary[0],
        'Q1': summary[1],
        'median': summary[2],
        'Q3': summary[3],
        'max': summary[4]
    }

print(five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
