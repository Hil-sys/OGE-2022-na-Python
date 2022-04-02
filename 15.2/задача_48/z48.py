s = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 6 == 0 and a % 10 == 4:
        s.append(a)
print(sum(s))