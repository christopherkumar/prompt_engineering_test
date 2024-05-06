def five_number_summary(data):
    """
    Returns the five-number summary of the given list of numbers.

    Parameters:
        data (list of int/float): The list of numbers to summarize.

    Returns:
        A dictionary containing the min, 25th percentile (Q1), median, 75th percentile (Q3), and max of the data.

    Raises:
        ValueError: If the data is empty.
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty.")

    data = sorted(data)
    min_val = data[0]
    max_val = data[-1]
    median = statistics.median(data)
    q1 = statistics.median(data[:len(data) // 2])
    q3 = statistics.median(data[(len(data) + 1) // 2:])

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
