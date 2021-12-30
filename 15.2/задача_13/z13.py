s = []
k = 0
sr = 0
b = 1
#t = '{:.' + str(b) + 'f}'   так тоже можно, будет надежней, но сложнее запомнить. print(t.format(sr))
while True:
    a = int(input())
    if a == 0:
        break
    if a % 8 == 0:
        s.append(a)
        k += 1
if len(s) == 0:
    print('NO')
else:
    sr = sum(s) / k
#    print(t.format(sr))
    print(round(sr,1))