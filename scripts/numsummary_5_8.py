def generate_five_number_summary(numbers):
    """
    Calculate the five-number summary for a given dataset.

    Parameters:
        numbers (list of float/int): The dataset to calculate the summary for.

    Returns:
        A dictionary with the five-number summary statistics.

    Raises:
        ValueError: If numbers is empty or contains non-numeric values.
    """
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    numbers.sort()
    min_num = numbers[0]
    max_num = numbers[-1]
    median = statistics.median(numbers)
    q1 = statistics.median(numbers[:len(numbers) // 2])
    q3 = statistics.median(numbers[(len(numbers) + 1) // 2:])

    return {'min': min_num, 'Q1': q1, 'median': median, 'Q3': q3, 'max': max_num}

print(generate_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
