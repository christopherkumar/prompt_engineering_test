def five_number_summary(data):
    """
    Calculate the five number summary of a list of numbers.

    Parameters:
        data (list): A list of numbers to summarize.

    Returns:
        A list with the minimum, first quartile, median, third quartile, and maximum of the data.
    """
    if not data or type(data) != list or not all(isinstance(n, (int, float)) for n in data):
        raise ValueError("Input must be a list of numbers")
    data.sort()
    q1 = data[len(data) // 4]
    median = data[len(data) // 2]
    q3 = data[3 * len(data) // 4]

    return [data[0], q1, median, q3, data[-1]]

print(five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
