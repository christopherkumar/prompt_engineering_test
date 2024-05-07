def robust_five_number_summary(data):
    """
    Computes the five-number summary of the provided data set.

    Parameters:
        data (list of int/float): The dataset for the summary calculation.

    Returns:
        A dictionary containing the five-number summary: min, Q1, median, Q3, and max.

    Raises:
        ValueError: If the data list is empty or contains invalid elements.
    """
    if not data or not all(isinstance(num, (int, float)) for num in data):
        raise ValueError("Data must be a list of integers or floats and cannot be empty.")

    data.sort()
    min_val = data[0]
    q1 = np.percentile(data, 25)
    median = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    max_val = data[-1]

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(robust_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
