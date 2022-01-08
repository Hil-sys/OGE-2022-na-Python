s = []
while True:
    a = int(input())
    if a == 3:
        break
    if (a % 7 == 0) and (a % 10 == 2):
        s.append(a)
print(sum(s))
