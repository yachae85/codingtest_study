from collections import deque
import sys

n, m, d = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
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


def bfs(archer, field):
    x, y = 0, 1
    q = deque()
    visited = [[False for __ in range(m)] for _ in range(n)]
    q.append((n-1, archer))
    kill = 0

    while q:
        pos = q.popleft()

        visited[pos[x]][pos[y]] = True
        if field[pos[x]][pos[y]] == 1:
            kill += 1
            field[pos[x]][pos[y]] = 0
            break

        for i in range(3):
            tx = pos[x] + dx[i]
            ty = pos[y] + dy[i]

            if tx < 0 or ty < 0 or ty >= m:
                continue
            if get_distance(n, archer, tx, ty) > d:
                continue
            if not visited[tx][ty]:
                q.append((tx, ty))

    return kill


get_archer_combination([], 0, 0)

result = -sys.maxsize
first_enemy = sum(sum(row) for row in field)
for archers in archer_combination:
    enemy = first_enemy
    kill = 0
    cp = [row[:] for row in field]
    while enemy > 0:
        # attack
        for archer in archers:
            k = bfs(archer, cp)
            enemy -= k
            kill += k
        # move_down
        cp.insert(0, [0 for _ in range(m)])
        eleminated = cp.pop()
        enemy -= eleminated.count(1)
    result = max(kill, result)

print(result)
