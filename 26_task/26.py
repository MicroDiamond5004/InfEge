import random
with open("26_1.txt", "w") as F:
    k = 10
    for line in range(1, 50):
        F.write(str(random.randint(1, k)) + " " + str(random.randint(1, k)) + "\n")

