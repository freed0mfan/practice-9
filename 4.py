N = ''
possible = 0
while N != 0:
    N = int(input('N: '))
    if N != 0 and N % 2 == 0:
        possible += 1
print(possible)
