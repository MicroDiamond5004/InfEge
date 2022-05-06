with open("27_task/27-B.txt") as F:
    n = int(F.readline())
    k5 = 0
    k7 = 0
    maxSum = 0
    totalSum = 0
    minTails = {0 : 0}
    for i in range(0, n):
        line = int(F.readline())
        totalSum += line
        if line % 5 == 0:
            k5 += 1
        if line % 7 == 0:
            k7 += 1
        if abs(k7 - k5) not in minTails:
            minTails[abs(k7 - k5)] = totalSum
        else:
            minT = minTails[abs(k7 - k5)]
            if totalSum - minT > maxSum:
                maxSum = totalSum - minT
    print(maxSum)