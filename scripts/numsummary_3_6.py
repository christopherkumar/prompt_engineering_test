def FiveNumberSummary(list_of_numbers):
    list_of_numbers.sort()
    return [
        list_of_numbers[0],
        list_of_numbers[len(list_of_numbers)//4],
        list_of_numbers[len(list_of_numbers)//2],
        list_of_numbers[3*len(list_of_numbers)//4],
        list_of_numbers[-1]
    ]

print(FiveNumberSummary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
