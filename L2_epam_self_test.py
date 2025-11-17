# Numbers

import math
import random

# modulus
a = 580 % 41
print(a)

# Exponentiation
b = 67 ** 6
print(b)

# Floor Division
c = 580 // 41
print(c)

d = [3, 5, "they"]
print(random.choice(d))

balance = 0.0
for _ in range(0, 10):
    balance += 0.1
    print(balance)

if math.isclose(balance, 1.0):
    print(balance)
    print("The balance is close enough to one.")
else:
    print("The balance is NOT one... it's something else.")
    print(balance)