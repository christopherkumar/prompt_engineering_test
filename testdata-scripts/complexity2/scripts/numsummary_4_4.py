def get_five_number_summary(numbers):
    """
    Calculates the five number summary (min, Q1, median, Q3, max) of a list of numbers.

    :param numbers: list of numerical values
    :return: A list containing the five number summary of the input list.
    """
    numbers.sort()
    min_val = numbers[0]
    max_val = numbers[-1]
    median = numbers[len(numbers) // 2]
    q1 = numbers[len(numbers) // 4]
    q3 = numbers[3 * len(numbers) // 4]

    return [min_val, q1, median, q3, max_val]

print(get_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
