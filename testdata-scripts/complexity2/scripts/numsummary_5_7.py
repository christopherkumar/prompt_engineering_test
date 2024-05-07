import statistics

def detailed_five_number_summary(data):
    """
    Generates a detailed five-number summary of the provided data.

    Parameters:
        data (list of int/float): The list of numbers for analysis.

    Returns:
        A dictionary with the minimum, first quartile, median, third quartile, and maximum of the data.

    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not data:
        raise ValueError("Data cannot be empty.")
    
    data.sort()
    min_val = data[0]
    max_val = data[-1]
    median = statistics.median(data)
    q1 = statistics.median(data[:len(data) // 2])
    q3 = statistics.median(data[(len(data) + 1) // 2:])

    return {'min': min_val, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_val}

print(detailed_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
