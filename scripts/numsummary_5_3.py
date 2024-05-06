import statistics

def calculate_five_number_summary(data):
    """
    Compute the five number summary of the given dataset.

    Parameters:
        data (list of int/float): The data set to analyze.

    Returns:
        A dictionary with keys 'min', 'Q1', 'median', 'Q3', 'max' representing the five number summary.

    Raises:
        ValueError: If the data list is empty.
    """
    if not data:
        raise ValueError("Data list must not be empty.")

    data.sort()
    min_val = min(data)
    max_val = max(data)
    median = statistics.median(data)
    q1 = statistics.median(data[:len(data)//2])
    q3 = statistics.median(data[len(data)//2:])

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(calculate_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
