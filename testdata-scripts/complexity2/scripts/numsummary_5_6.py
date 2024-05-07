def get_five_number_summary(data):
    """
    Compute the five-number summary for a list of numerical data.

    Args:
        data (list of int/float): Data list to analyze.

    Returns:
        A dictionary containing the five-number summary.

    Raises:
        ValueError: For invalid input types or empty lists.
    """
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list of numbers.")

    sorted_data = sorted(data)
    min_val = sorted_data[0]
    max_val = sorted_data[-1]
    median = statistics.median(sorted_data)
    q1 = statistics.median(sorted_data[:len(sorted_data) // 2])
    q3 = statistics.median(sorted_data[(len(sorted_data) + 1) // 2:])

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(get_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
