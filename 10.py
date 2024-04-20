n = int(input('n: '))
ladders = 1
previous = n
current = 0
while previous > 2:
    while current < previous - 1:
        previous -= 1
        current += 1
        if current != previous:
            ladders += 1
    previous = current
    current = 0
print(ladders)
