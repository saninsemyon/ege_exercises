f = open('../../files_for_tasks/28141.txt')
vmestimost, n = map(int, f.readline().split())
korobki = []
for s in f:
    korobki.append(int(s))
korobki.sort()
korobki_sudno = []
for count in range(len(korobki)):
    if sum(korobki_sudno) + korobki[count] <= vmestimost:
        korobki_sudno.append(korobki[count])
    elif sum(korobki_sudno[:-1]) + korobki[count] <= vmestimost:
        del korobki_sudno[-1]
        korobki_sudno.append(korobki[count])
print(len(korobki_sudno), max(korobki_sudno))

