for k in range(0, 1000000, 2):
    m = 900000000 + k
    a0 = 0
    while m % 2 == 0:
        a0 += 1
        m //= 2
    if a0 % 2 != 0 and int(m ** 0.5) == m ** 0.5:
        print(k)