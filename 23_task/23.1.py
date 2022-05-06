def F(start, end):
    if start > end:
        return 0
    elif start == end:
        return 1
    elif start < end:
        return F(start + 1, end) + F(start + 2, end)

print(F(1, 5))