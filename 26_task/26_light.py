with open("26_1.txt") as F:
    empty = F.readline()
    num = 10000
    sqare = ["0" * num] * num
    lines = []
    dx = dict()
    listY = []
    countX = 0
    d = dict()
    k = 0
    l = 0
    finishD = dict()
    maxDistance = 0
    maxCount = 0
    for line in F:
        lines.append(line.split())
    for i in lines:
        y = int(i[0])
        x = int(i[1])
        xCoord = sqare[y - 1]
        xCoordEnd = ""
        for j in range(0, num):
            xCoordEnd += xCoord[j]
            if j == x - 1:
                xCoordEnd += "!"
                xCoordEnd = xCoordEnd.replace(xCoord[j] + "!", "1")
        sqare[y - 1] = xCoordEnd
    for i in range(0, num - 1):
        before = ""
        for j in sqare:
            before += j[i]
        listY.append(before)
    for i in sqare:
        l += 1
        distance = [0] * 2
        count = 1
        flag = True
        for searchX in range(0, num - 1):
            if i[searchX] == "1" and i[searchX + 1] == "1":
                count += 1
                if flag == True:
                    distance[0] = searchX
                    flag = False
                if searchX == num - 2:
                    distance[1] = num - searchX - 2
                    d[k] = str(distance[0]) + " " + str(distance[1]) + " " + str(count) + " " + str(l)
                    count = 1
                    distance = [0] * 2
                    flag = True
            elif i[searchX] == "0" and count > 1:
                distance[1] = num - searchX
                d[k] = str(distance[0]) + " " + str(distance[1]) + " " + str(count) + " " + str(l)
                count = 1
                distance = [0] * 2
                flag = True
            elif i[searchX + 1] == "0" and count > 1:
                distance[1] = num - searchX - 1
                d[k] = str(distance[0]) + " " + str(distance[1]) + " " + str(count) + " " + str(l)
                count = 1
                distance = [0] * 2
                flag = True
            k += 1
    kI = 0
    for i in d:
        s = d[i]
        s = s.split()
        finishD[kI] = s[2] + " " + str(min(s[0], s[1])) + " " + str(int(s[3]) - 1) + " " + str(num - int(s[3]))
        kI += 1
    print(finishD)
    for i in finishD:
        s = finishD.get(i).split()
        print(s, int(s[1]))
        if int(s[0]) >= maxCount:
            maxCount = int(s[0])
            if min(int(s[1]), int(s[2]), int(s[3])) > maxDistance:
                maxDistance = min(int(s[1]), int(s[2]), int(s[3]))
    print(maxCount, maxDistance)