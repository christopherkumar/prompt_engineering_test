def calculate_summary(numbers):
    """
    Calculates the five number summary for a given list of numbers.

    Args:
        numbers (list): List of numbers for which to calculate the summary.

    Returns:
        list: Contains the minimum, first quartile, median, third quartile, and maximum of the list.
    """
    numbers.sort()
    q1 = numbers[int(len(numbers) * 0.25)]
    q3 = numbers[int(len(numbers) * 0.75)]
    median = numbers[len(numbers) // 2]
    return [numbers[0], q1, median, q3, numbers[-1]]

print(calculate_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
