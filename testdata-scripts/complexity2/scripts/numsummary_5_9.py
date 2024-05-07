import numpy as np

def optimal_five_number_summary(data):
    """
    Calculate the five-number summary of a data set using numpy for efficiency.

    Parameters:
        data (list of int/float): Data set to analyze.

    Returns:
        A dictionary with keys 'min', 'Q1', 'median', 'Q3', and 'max' representing the summary.

    Raises:
        ValueError: If data is empty or not a list of numbers.
    """
    if not isinstance(data, list) or not data:
        raise ValueError("Data must be a non-empty list of numbers.")
    
    summary = np.percentile(data, [0, 25, 50, 75, 100])

    return {
        'min': summary[0],
        'Q1': summary[1],
        'median': summary[2],
        'Q3': summary[3],
        'max': summary[4]
    }

print(optimal_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
