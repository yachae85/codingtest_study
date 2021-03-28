from itertools import combinations


def get_distance(pos_1, pos_2) :
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])


def attack(enemies, pos, d):
    min_d = 11
    min_pos = (21,21)

    for i in range(len(enemies)-1,-1,-1) :
        for j in range(len(enemies[i])) :
            cur_d = get_distance(pos, (i,j))
            if cur_d <= d and cur_d <= min_d and enemies[i][j] == 1 :
                if cur_d == min_d and j >= min_pos[1] : continue
                min_d = cur_d
                min_pos = (i,j)

    return min_pos

N,M,D=input().split()
N = int(N)
M = int(M)
D = int(D)

enemies = list()
enemies2 = list()

## Map을 입력받음
for i in range(N) :
    cur_enemies = input().split()
    cur_enemies = [ int(cur_enemy) for cur_enemy in cur_enemies ]
    cur_enemies2 = [ cur_enemy for cur_enemy in cur_enemies ]
    enemies.append(cur_enemies)
    enemies2.append(cur_enemies2)

enemies.reverse()
enemies2.reverse()

## 궁수의 조합 생성
cols = [ i for i in range(M)]
combs = list(combinations(cols, 3))

## 탐색 시작
max_len = 0
## 궁수 조합 지정
for comb in combs :
    cur_len = 0
    ## 탐색 횟수 지정
    for i in range(N) :
        attacked = set()
        ## 궁수가 공격할 대상 선정
        for j in comb :
            a = attack(enemies[i:], (-1,j), D)
            attacked.add(attack(enemies[i:], (-1,j), D))
        attacked = attacked - set([(21,21)])
        cur_len += len(attacked)
        ## 공격받은 적 제외
        for cur_pos in attacked :
            enemies[i+cur_pos[0]][cur_pos[1]] = 0
    if max_len < cur_len :
        max_len = cur_len
    enemies = [[enemies2[i][j] for j in range(len(enemies2[i]))] for i in range(len(enemies2))]


print(max_len)
