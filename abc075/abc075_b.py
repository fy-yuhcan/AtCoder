DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

H, W = map(int, input().split())

S = [input() for _ in range(H)]

result = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            result[i][j] = "#"
        else:
            count = 0
            for dx, dy in zip(DX, DY):
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "#":
                    count += 1
            result[i][j] = count
for row in result:
    print("".join(map(str, row)))