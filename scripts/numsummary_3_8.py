def summary_of_numbers(numbers):
    numbers.sort()
    median = numbers[len(numbers) // 2]
    return [
        numbers[0],
        numbers[len(numbers) // 4], 
        median, 
        numbers[(3 * len(numbers)) // 4], 
        numbers[-1]
    ]

print(summary_of_numbers([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
