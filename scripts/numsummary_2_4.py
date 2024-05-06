def get_summary(data):
    data.sort()
    return [data[0], data[10], data[20], data[30], data[-1]]
print(get_summary([9, 27, 81, 86, 23, 30, 57, 31, 53, 0]));
