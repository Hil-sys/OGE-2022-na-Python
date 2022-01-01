s = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 7 == 0:
        s.append(a)
print(len(s))