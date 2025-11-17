# mutable vs immutable, data types

a = 257
b = a

x = [1, 2, 3]
y = x

b = b + 1
y.append(4)

print(a, b, x, y)
print(id(a), id(b), id(x), id(y))