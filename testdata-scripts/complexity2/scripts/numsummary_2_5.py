def FiveNumSummary(nums):
    if len(nums) == 0: return None
    return [min(num), max(nums)]
print(FiveNumSummary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
