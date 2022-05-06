with open("27-B.txt") as F:
    countAll = int(F.readline())
    d = [int(x) for x in F]
    i1 = len(d) // 2
    minIndex = 0
    summ = 0
    minSum = 99999999999999999999999999999999999999999999999999999
    dif = 0
    km = 0
    addIndex = 1
    minusIndex = i1 + 1
    for i in range(0, countAll):
        km = min(i, countAll - i)
        summ += km * d[i]
    minSum = min(summ, minSum)
    for i in range(1, countAll + 1):
        if i <= countAll // 2:
            dif -= d[i]
        else:
            dif += d[i % countAll]
    summ += dif
    minSum = min(summ, minSum)
    for i in range(2, countAll):
        dif += 2 * d[addIndex] - 2 * d[minusIndex]
        summ += dif
        if summ < minSum:
            minSum = summ
            minIndex = i + 1
        addIndex += 1
        minusIndex = (minusIndex + 1) % countAll
    print(minSum, minIndex)