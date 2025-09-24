def suma(x, y):
    totsum = 0
    start = min(x, y)
    end = max(x, y)
    for i in range(start, end + 1):
        if i % 3 == 0:
            totsum += i
    return totsum