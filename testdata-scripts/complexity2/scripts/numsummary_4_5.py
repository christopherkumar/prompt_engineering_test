def five_num_summary(list_of_nums):
    """
    Calculate the 5 number summary of a list of numbers.

    Parameters:
    list_of_nums (list): List of integers or floats.

    Returns:
    list: The 5 number summary [min, Q1, median, Q3, max].
    """
    list_of_nums.sort()
    min_num = list_of_nums[0]
    max_num = list_of_nums[-1]
    median = list_of_nums[len(list_of_nums) // 2]
    q1 = list_of_nums[len(list_of_nums) // 4]
    q3 = list_of_nums[3 * len(list_of_nums) // 4]

    return [min_num, q1, median, q3, max_num]

print(five_num_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
