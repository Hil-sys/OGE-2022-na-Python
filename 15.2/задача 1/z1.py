s = []
while True:
   n = int(input())
   if n == 0:
      break
   s.append(n)
s.sort()
sm = s[:2]
sx = s[-2:]
print(sum(sx), sum(sm))