def summary_stats(nums):
    if not nums:
        return None
    nums.sort()
    mid = len(nums) // 2
    return [nums[0], nums[mid // 2], nums[mid], nums[mid + mid // 2], nums[-1]]

print(summary_stats([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
