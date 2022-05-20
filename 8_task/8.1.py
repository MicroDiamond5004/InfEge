from itertools import product
count = 0
for i in product("0123456", repeat=7):
    word = "".join(i)
    if word[0] in "350":
        continue
    if "22" in word and "44" in word:
        continue
    count += 1
print(count)