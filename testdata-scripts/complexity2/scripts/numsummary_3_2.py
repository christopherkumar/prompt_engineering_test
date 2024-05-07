def calculate_summary(numbers):
    numbers.sort()
    return [
        numbers[0],
        numbers[len(numbers) // 4],
        numbers[len(numbers) // 2],
        numbers[3 * len(numbers) // 4],
        numbers[-1]
    ]

print(calculate_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
