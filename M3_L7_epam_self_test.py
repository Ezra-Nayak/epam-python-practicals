# Tuples

"""(a, b, c) = (40, 56.6, 90)
print(a, b, c)

a, b = 1, 2
print(a, b)

b, a = a, b
print(a, b)

x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)
print(id(x), id(y))
print(x is y)"""

def get_data_summary(data):

    if len(data) != 0:
        data.sort()
        sum_data = 0
        for num in data:
            sum_data += num
        return data[0], data[-1], sum_data
    else:
        return None, None, 0

smallest, largest, total = (get_data_summary([23, 12, 67, 123, 99]))

print(smallest, largest, total)
