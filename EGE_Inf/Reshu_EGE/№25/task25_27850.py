for count in range(245690, 245756 + 1):
    a = []
    for j in range(1, count):
        if count // 1 == count and count // count == 1:
            a.append(j)
        if len(a) > 2:
            break
    if len(a) == 2:
        print(a)