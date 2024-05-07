def summary_calculation(numbers):
    numbers.sort()
    return [min(numbers), numbers[10], numbers[20], numbers[30], max(numbers)]
print(summary_calculation([9, 27, 81, 86, 23, 30, 57, 31 53, 0]))
