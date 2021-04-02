
# boj g3 스터디문제
import sys
n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
memo = [[0] * n for _ in range(n)]
result = 0


def dfs(r, c):
    if memo[r][c] > 0:
        return memo[r][c]
    memo[r][c] = 1

    for d in range(4):
        tx = r + dx[d]
        ty = c + dy[d]

        if tx < 0 or tx >= n or ty < 0 or ty >= n:
            continue
        if b[r][c] >= b[tx][ty]:
            continue
        memo[r][c] = max(dfs(tx, ty) + 1, memo[r][c])

    # dead
    return memo[r][c]


for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
