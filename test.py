with open("27_task/27-B.txt") as F:
    countAll = int(F.readline())
    maxNum = dict()
    NumD = []
    minSum = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    d = [int(x) for x in F]
    countU = 0
    for u in range(0, len(d)):
        summ = 0
        def roundIndexPlus(x, plus):
            if x + plus <= len(d) - 1:
                return x + plus
            else:
                return 0 + abs((len(d) - 1) - (x + plus)) - 1
        def roundIndexMinus(x, minus):
            if x - minus >= 0:
                return x - minus
            else:
                return len(d) - abs(x - minus)
        minusCount = 0
        plusCount = 0
        for i in range(500000):
            plusCount += 1
            summ += d[roundIndexPlus(u, plusCount)] * plusCount
        for i in range(500000):
            minusCount += 1
            summ += d[roundIndexMinus(u, minusCount)] * minusCount
        if summ < minSum:
            minSum = summ
            countU = u + 1
    print(countU)
