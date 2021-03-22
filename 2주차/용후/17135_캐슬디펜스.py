# boj g4
from collections import deque
import sys

n, m, d = map(int, input().split())
origin_field = [list(map(int, input().split())) for _ in range(n)]
archer_combination = []

dx = [0, -1, 0]
dy = [-1, 0, 1]


def get_archer_combination(comb, d, start):
    if d == 3:
        archer_combination.append(comb[:])
    for i in range(start, m):
        comb.append(i)
        get_archer_combination(comb, d+1, i+1)
        comb.pop()


def get_distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)


def attack(archer, field, dead):
    q = deque()
    visited = [[False for __ in range(m)] for _ in range(n)]
    q.append((n-1, archer))

    while q:
        pos = q.popleft()
        x = pos[0]
        y = pos[1]
        visited[x][y] = True

        if field[x][y] == 1:
            dead.add((x, y))
            return

        for i in range(3):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx < 0 or ty < 0 or ty >= m:
                continue
            if visited[tx][ty]:
                continue
            if get_distance(n, archer, tx, ty) > d:
                continue
            q.append((tx, ty))


get_archer_combination([], 0, 0)
result = -sys.maxsize

for archers in archer_combination:
    kill = 0
    field = [row[:] for row in origin_field]

    for _ in range(n):
        dead = set()
        for archer in archers:
            attack(archer, field, dead)
        for ex, ey in dead:
            kill += 1
            field[ex][ey] = 0
        field.pop()
        field.insert(0, [0]*m)
    result = max(kill, result)
print(result)
