for count in range(123456789, 223456789 + 1):
    cnt = 0
    spis = []
    for n in range(2, count):
        if count % n == 0:
            cnt += 1
            spis.append(n)
        if cnt > 3:
            break
    if cnt == 3:
        print(count, spis)