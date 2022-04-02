n = int(input())
s = []
s1 = []
for i in range(n):
    a = int(input())
    s.append(a)
    if a <= 30:
        s1.append(a)
print(max(s)-min(s))
print(len(s1))