N = int(input('N: '))
group = 2
while N % group != 0:
    group += 1
print(group)
