def five_number_summary(data):
    data.sort()
    q2 = data[len(data) // 2]
    q1 = data[len(data) // 4]
    q3 = data[(3 * len(data)) // 4]
    return [min(data), q1, q2, q3, max(data)]

print(five_number_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
