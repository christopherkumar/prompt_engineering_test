def compute_five_number_summary(nums):
    """
    Compute the five number summary of a list of numbers.

    Args:
    nums (list): List of numbers to calculate the summary.

    Returns:
    A list containing the minimum, lower quartile, median, upper quartile, and maximum of the numbers.
    """
    if len(nums) == 0:
        return []
    nums.sort()
    min_num = nums[0]
    max_num = nums[-1]
    mid = len(nums) // 2
    median = nums[mid]
    q1 = nums[mid // 2]
    q3 = nums[(mid + len(nums)) // 2]

    return [min_num, q1, median, q3, max_num]

print(compute_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
