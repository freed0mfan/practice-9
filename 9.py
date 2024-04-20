n = int(input('n: '))
dots = 0
for x in range(0, n + 1):
    for y in range(0, n + 1):
        if x == y:
            dots += 2 * x
        if x != y:
            dots += 0.5 * (x + y)
print(int(dots))
