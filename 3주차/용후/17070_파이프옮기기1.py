# boj g5

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
VERTICAL = 0
HORIZONTAL = 1
DIAGONAL = 2
result = 0


def check_bound(r, c):
    return r < n and c < n


def dfs(state, r, c):
    global result
    if r == n-1 and c == n-1:
        result += 1
        return

    if state == HORIZONTAL or state == DIAGONAL:
        if check_bound(r, c+1) and board[r][c+1] == 0:
            dfs(HORIZONTAL, r, c+1)
    if state == VERTICAL or state == DIAGONAL:
        if check_bound(r+1, c) and board[r+1][c] == 0:
            dfs(VERTICAL, r+1, c)
    if check_bound(r+1, c+1) and board[r][c+1] == 0 and board[r+1][c+1] == 0 and board[r+1][c] == 0:
        dfs(DIAGONAL, r+1, c+1)


dfs(HORIZONTAL, 0, 1)
print(result)
