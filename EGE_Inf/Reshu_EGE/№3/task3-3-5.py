num = int(input())
num > 0
hrs = num // 3600
mm = (num - hrs * 3600) // 60
secs = num % 60
print(str(hrs) + ':' + str(mm) + ':' + str(secs))