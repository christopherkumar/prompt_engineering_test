def get_five_number_summary(data):
    """
    Calculate the five-number summary for a list of numerical data.

    Args:
        data (list): The data to calculate the summary for, must be a list of numbers.

    Returns:
        A dictionary containing the five-number summary statistics.

    Raises:
        TypeError: If the input data is not a list or contains non-numeric elements.
        ValueError: If the list is empty.
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("Input must be a list of numeric values.")
    if len(data) == 0:
        raise ValueError("Input list cannot be empty.")
    
    data.sort()
    min_val = data[0]
    q1 = data[len(data) // 4]
    median = data[len(data) // 2]
    q3 = data[3 * len(data) // 4]
    max_val = data[-1]

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(get_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
