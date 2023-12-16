for i in range(0, 256):
    b = str(bin(i)[2:].zfill(8))
    b.replace('0', 'i')
    b.replace('1', '0')
    b.replace('i', '1')
    a = int(b, 2)
    if i - a == 111:
        print(i)
        break