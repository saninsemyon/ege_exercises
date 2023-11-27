f = open('../../Файлы_для_задач/28141.txt')
vmestimost, n = map(int, f.readline().split())
korobki = []
for s in f:
    korobki.append(int(s))
korobki.sort()
korobki_sudno = []
for i in range(len(korobki)):
    if sum(korobki_sudno) + korobki[i] <= vmestimost:
        korobki_sudno.append(korobki[i])
    elif sum(korobki_sudno[:-1]) + korobki[i] <= vmestimost:
        del korobki_sudno[-1]
        korobki_sudno.append(korobki[i])
print(len(korobki_sudno), max(korobki_sudno))

