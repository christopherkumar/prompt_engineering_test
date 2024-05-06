def summary(data):
    data.sort()
    return [
        data[0],
        data[len(data) // 4 - 1],
        data[len(data) // 2],
        data[3 * len(data) // 4 - 1],
        data[-1]
    ]

print(summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]))
