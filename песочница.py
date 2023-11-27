f = 32000
n = 32
t = 40 * 2 ** 23 // f * n * 2
v1 = 2 * f * n * t
v2 = 1 * f // 2 * n // 2 * t
x = v1 // v2
print(x)
