N = int(input())

# [0] = horizontal posture, [1] = vertical posture, [2] = diagonal posture
pos_mvs = [[0,2],[1,2],[0,1,2]]

# [0] = horizontal move, [1] = vertical move, [2] = diagonal move
pipe_mv = [(0,1,0),(1,0,1),(1,1,2)]




wall = list()
dp = [[[-1 for k in range(3)] for j in range(N+1)] for i in range(N+1)]
wall.append([0 for i in range(N+1)])
for i in range(1,N+1) :
    cur_row = input().split()
    cur_row = [0] + [int(cur_ele) for cur_ele in cur_row]
    wall.append(cur_row)

def check_move_possible_for_one_position(wall,r,c) :
    if r < 1 or r > N : return False
    if c < 1 or c > N  : return False
    if wall[r][c] == 1 : return False

    return True

def check_move_possible_for_one_posture(wall, new_r, new_c, new_pos) :
    if new_pos < 2 : return check_move_possible_for_one_position(wall, new_r, new_c)

    pos = check_move_possible_for_one_position(wall, new_r, new_c)
    pos = pos and check_move_possible_for_one_position(wall, new_r-1, new_c)
    pos = pos and check_move_possible_for_one_position(wall, new_r, new_c-1)

    return pos



def move_pipe(wall, cur_r, cur_c, cur_pose) :
    if cur_r == N and cur_c == N : return 1

    if dp[cur_r][cur_c][cur_pose] > -1 : return dp[cur_r][cur_c][cur_pose]

    dp[cur_r][cur_c][cur_pose] = 0

    for pos_mv in pos_mvs[cur_pose] :
      new_r = cur_r + pipe_mv[pos_mv][0]; new_c = cur_c + pipe_mv[pos_mv][1]
      new_pos = pipe_mv[pos_mv][2]
      if check_move_possible_for_one_posture(wall, new_r, new_c, new_pos) == False : continue

      dp[cur_r][cur_c][cur_pose] += move_pipe(wall,new_r,new_c,new_pos)

    return dp[cur_r][cur_c][cur_pose]

print(move_pipe(wall,1,2,0))