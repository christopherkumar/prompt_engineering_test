def summary(numbers):
    if not numbers: return []
    return [numbers[0], numbers[-1]]
print summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0])
