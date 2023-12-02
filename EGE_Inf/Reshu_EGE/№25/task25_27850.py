for i in range(245690, 245756 + 1):
    a = []
    for j in range(1, i):
        if i // 1 == i and i // i == 1:
            a.append(j)
        if len(a) > 2:
            break
    if len(a) == 2:
        print(a)