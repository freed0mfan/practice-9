for n in range(10, 100):
    if len(str(n ** 2)) == 3 and n ** 2 % 100 == n:
        print(n ** 2)
