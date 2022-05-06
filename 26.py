with open("26_1.txt") as F:
    amount, summ = map(int, F.readline().split())
    d = []
    for line in F:
        d.append(line.split())
    d.sort()
    list_Z = [int(x[0]) for x in d if x[1] == "Z"]
    list_Q = [int(x[0]) for x in d if x[1] == "Q"]
    zq = dict()
    curSum = 0
    sumZ = []
    for i in range(0, len(d)):
        pair = d[i]
        word = pair[1]
        curSum = int(pair[0]) + curSum
        zq[word] = zq.get(word, 0) + 1
        if curSum > summ:
            curSum -= int(pair[0])
            zq[word] = zq.get(word, 0) - 1
            break
    list_Z = sorted(list_Z[:zq.get("Z")], reverse = True)
    list_Q = list_Q[zq.get("Q"):]
    for i in range(0, len(list_Z)):
        if curSum - list_Z[i] + list_Q[i] <= summ:
            curSum -= list_Z[i] - list_Q[i]
            zq["Q"] = zq.get("Q") + 1
            zq["Z"] = zq.get("Z") - 1
    print(zq.get("Q"), summ - curSum)