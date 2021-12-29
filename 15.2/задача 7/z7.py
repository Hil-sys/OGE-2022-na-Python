s = []
k = 0
while True:
    a = int(input())
    if a == 0:
        break
    s.append(a)
    if (a % 2 == 1) and (a % 3 == 0):
        k += 1
print(len(s))
print(k)