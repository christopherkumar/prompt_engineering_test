def five_num_summary(data):
    data.sort()
    q1 = data[int(len(data) * 0.25)]
    q3 = data[int(len(data) * 0.75)]
    median = data[int(len(data) * 0.5)]
    return [data[0], q1, median, q3, data[-1]]

print(five_num_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
