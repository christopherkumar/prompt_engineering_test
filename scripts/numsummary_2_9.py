def five_number(data):
    data.sort()
    return [data[0], data[1], data[2], data[3], data[4]]
print(five_number([9, 27, 81, 86, 23, 30, 57, 31, 53, 0])))
