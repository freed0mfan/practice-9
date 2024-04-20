for n in range(1000000):
    start = (6 - len(str(n))) * '0' + str(n)
    one = (6 - len(str(n + 1))) * '0' + str(n + 1)
    two = (6 - len(str(n + 2))) * '0' + str(n + 2)
    three = (6 - len(str(n + 3))) * '0' + str(n + 3)
    if start[1:] == start[-1:-6:-1] and one[1:] == one[-1:-6:-1] and two[1:5] == two[-2:-6:-1] and three == three[-1::-1]:
        print(n) #199999
