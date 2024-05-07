def get_five_number_summary(data):
    if len(data) == 0:
        return []
    data.sort()
    median = data[len(data) // 2]
    lower_quartile = data[len(data) // 4]
    upper_quartile = data[3 * len(data) // 4]
    return [min(data), lower_quartile, median, upper_quartile, max(data)]

print(get_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
