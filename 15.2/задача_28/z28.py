s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 5 == 0) and (a % 2 == 0):
        s.append(a)
print(len(s))