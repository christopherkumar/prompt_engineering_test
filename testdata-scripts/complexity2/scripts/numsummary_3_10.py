def calc_five_number_summary(data):
    if len(data) < 5:
        return "Not enough data"
    data.sort()
    q1 = data[len(data) // 4]
    q3 = data[3 * len(data) // 4]
    median = data[len(data) // 2]
    return [min(data), q1, median, q3, max(data)]

print(calc_five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
