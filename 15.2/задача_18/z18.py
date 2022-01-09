s = []
sr = 0
while True:
    a = int(input())
    if a == 0:
        break
    if (9 < a) and (a < 100):
        s.append(a)
if len(s) == 0:
    print('NO')
else:
    sr = sum(s) / len(s)
    print(round(sr,1))
