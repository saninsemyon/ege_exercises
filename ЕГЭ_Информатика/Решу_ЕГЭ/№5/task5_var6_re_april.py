for nums in range(1000, 10000):
    g = str(nums)
    k1 = int(g[0]) + int(g[1])
    k2 = int(g[1]) + int(g[2])
    k3 = int(g[2]) + int(g[3])
    first = str((k1 + k2 + k3) - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    b = first + second
    if b == '1517':
        print(nums)
        break