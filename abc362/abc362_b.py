a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d= (a[0]-b[0])**2 + (a[1]-b[1])**2
e= (b[0]-c[0])**2 + (b[1]-c[1])**2
f= (c[0]-a[0])**2 + (c[1]-a[1])**2
g= [d,e,f]
g.sort()
if g[2] == g[0]+g[1]:
  print("Yes")
else:
  print("No")