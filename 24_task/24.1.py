with open("24 (2).txt") as F:
    line = F.readline()
    line = line.replace("D", "C")
    subline = line.split("C")
    length = 0
    for i in range(0, len(subline) - 3):
        currentLine = subline[i] + "C" + subline[i + 1] + "C" + subline[i + 2] + "C" + subline[i + 3]
        length = max(length, len(currentLine))
    print(length)