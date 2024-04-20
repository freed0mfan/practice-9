import math

num = float(input('Положительное число больше 2: '))
while num >= 2:
    num = math.sqrt(num)
    print(f'{num:.3f}')
