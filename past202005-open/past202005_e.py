N, M, Q = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

col = list(map(int, input().split()))

for i in range(Q):
    t, x, *y = map(int, input().split())
    x -= 1
    print(col[x])
    
    if t == 1:
        for v in G[x]:
            col[v] = col[x]
    else:
        col[x] = y[0]
