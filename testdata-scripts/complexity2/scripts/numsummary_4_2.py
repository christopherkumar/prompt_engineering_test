def five_number_summary(data):
    """
    Returns the five-number summary of the given data.

    Parameters:
    data (list of int): The list of numbers to summarize.

    Returns:
    tuple: Contains the minimum, first quartile, median, third quartile, and maximum of the data.
    """
    data = sorted(data)
    min_val = data[0]
    max_val = data[-1]
    median = data[len(data) // 2]
    q1 = data[len(data) // 4]
    q3 = data[3 * len(data) // 4]

    return min_val, q1, median, q3, max_val

print(five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
