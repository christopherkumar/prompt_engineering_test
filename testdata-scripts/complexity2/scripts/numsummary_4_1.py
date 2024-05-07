def calculate_five_number_summary(numbers):
    """
    Calculate the five-number summary for a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: The five-number summary (min, Q1, median, Q3, max).
    """
    if not numbers:
        return []
    numbers.sort()
    min_val = numbers[0]
    max_val = numbers[-1]
    median = numbers[len(numbers) // 2]
    q1 = numbers[len(numbers) // 4]
    q3 = numbers[(3 * len(numbers)) // 4]
    return [min_val, q1, median, q3, max_val]

print(calculate_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
