import numpy as np

def compute_five_number_summary(data):
    """
    Calculate the five number summary for a given list of numbers.

    Parameters:
        data (list): The list of numbers to process.

    Returns:
        A dictionary with keys 'min', 'Q1', 'median', 'Q3', and 'max'.

    Raises:
        ValueError: If the input is not a list or the list is empty.
    """
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    
    data = sorted(data)
    summary = np.percentile(data, [0, 25, 50, 75, 100])

    return {
        'min': summary[0],
        'Q1': summary[1],
        'median': summary[2],
        'Q3': summary[3],
        'max': summary[4]
    }

print(compute_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
