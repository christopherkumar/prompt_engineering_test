def summary_stats(data):
    """
    Generate the five-number summary for the given dataset.

    data: List of integers or floats.
    Returns the five-number summary as a list.
    """
    if len(data) == 0:
        return []
    data.sort()
    return [
        data[0],
        data[len(data) // 4],
        data[len(data) // 2],
        data[3 * len(data) // 4],
        data[-1]
    ]

print(summary_stats([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
