for i in range(128, 256):
   s = i.readline()
   if int(s) == 0:
       i.replace(0, 1)
   else:
       i.replace(1, 0)