import math

x = int(input('Натуральное число: '))
ways = 0
for n in range(1, int(math.sqrt(x)) + 1):
    for m in range(1, int(math.sqrt(x)) + 1):
        if n ** 2 + m ** 2 == x:
            ways += 1
print(ways // 2 + ways % 2)
