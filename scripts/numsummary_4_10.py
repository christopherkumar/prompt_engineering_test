def get_summary_statistics(nums):
    """
    Calculate the five-number summary of a list of numbers.

    Args:
        nums (list): The list of numbers.

    Returns:
        A list containing the minimum, first quartile, median, third quartile, and maximum.
    """
    if not nums:
        raise ValueError("List is empty")
    nums.sort()
    min_val = nums[0]
    max_val = nums[-1]
    median = nums[len(nums) // 2]
    q1 = nums[len(nums) // 4]
    q3 = nums[3 * len(nums) // 4]

    return [min_val, q1, median, q3, max_val]

print(get_summary_statistics([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
