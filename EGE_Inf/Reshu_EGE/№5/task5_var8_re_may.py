for count in range(128, 256):
   s = count.readline()
   if int(s) == 0:
       count.replace(0, 1)
   else:
       count.replace(1, 0)