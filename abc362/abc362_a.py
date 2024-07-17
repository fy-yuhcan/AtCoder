a = list(map(int,input().split()))
d = input()
if d == "Red":
  if a[1] < a[2]:
    print(a[1])
  else:
    print(a[2])
if d == "Green":
  if a[0] < a[2]:
    print(a[0])
  else:
    print(a[2])
if d == "Blue":
  if a[0] < a[1]:
    print(a[0])
  else:
    print(a[1])