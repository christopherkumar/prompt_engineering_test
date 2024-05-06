def summary(numbers):
    """
    Calculates the five-number summary for a set of numbers.

    Args:
        numbers (list): The numbers to calculate the summary for.

    Returns:
        A list containing the minimum, 1st quartile, median, 3rd quartile, and maximum of the numbers.
    """
    numbers.sort()
    return [
        numbers[0],
        numbers[len(numbers) // 4],
        numbers[len(numbers) // 2],
        numbers[3 * len(numbers) // 4],
        numbers[-1]
    ]

print(summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
