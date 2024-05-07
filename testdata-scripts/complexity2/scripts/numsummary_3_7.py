def compute_summary(nums):
    """Calculates the five number summary of a list of numbers."""
    nums.sort()
    return [
        nums[0], nums[len(nums) // 4], nums[len(nums) // 2], 
        nums[3 * len(nums) // 4], nums[-1]
    ]

print(compute_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
