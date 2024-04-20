for s in range(1, 10):
    for e in range(10):
        for n in range(10):
            for d in range(10):
                for m in range(1, 10):
                    for o in range(10):
                        for r in range(10):
                            for y in range(10):
                                digits = [s, e, n, d, m, o, r, y]
                                sum_times_appeared = 0
                                for digit in digits:
                                    sum_times_appeared += digits.count(digit)
                                if len(digits) == sum_times_appeared:
                                    send = int(str(s) + str(e) + str(n) + str(d))
                                    more = int(str(m) + str(o) + str(r) + str(e))
                                    money = int(str(m) + str(o) + str(n) + str(e) + str(y))
                                    if send + more == money:
                                        print(f'SEND = {send}\nMORE = {more}\nMONEY = {money}')

# SEND = 9567
# MORE = 1085
# MONEY = 10652
