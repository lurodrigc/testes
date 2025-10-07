import random

a = random.sample(range(1, 51), 6)
b = random.sample(range(1, 51), 8)

intersec = set(a) & set(b)
print(intersec)
