N, Q = map(int, input().split())
S = input()

cs = [0] * (N + 1)
for i in range(1, N):
    cs[i + 1] = cs[i] + (1 if S[i - 1:i + 1] == "AC" else 0)

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    print(cs[r] - cs[l + 1])
