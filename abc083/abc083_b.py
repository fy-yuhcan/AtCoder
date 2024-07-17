def ca(n):
  sum = 0
  while n >0:
    sum += n % 10
    n //= 10
  return sum
n,a,b = map(int,input().split())
result = 0
for i in range(1,n+1):
  if a<= ca(i) <= b:
    result += i

print(result)