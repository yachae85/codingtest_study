import sys
sys.setrecursionlimit(10**7)



n = int(sys.stdin.readline())

forest = []
mv = [(-1,0),(1,0),(0,-1),(0,1)]


for i in range(n) :
    cur_row = list(map(int,sys.stdin.readline().split()))
    forest.append(cur_row)

copied_forest = [[ cur_bamboos for cur_bamboos in forest[i]] for i in range(len(forest))]
dp = [[-1 for i in range(len(cur_cell))] for cur_cell in forest]

def roaming_forest(forest, dp, r, c) :
    if dp[r][c] > -1 : return dp[r][c]
    dp[r][c] = 1

    for row_mv, col_mv in mv :
        new_row = r + row_mv; new_col = c + col_mv;
        if new_row < 0 or new_row >= n : continue
        if new_col < 0 or new_col >= n : continue
        if forest[new_row][new_col] <= forest[r][c] : continue
        dp[r][c] = max(dp[r][c], roaming_forest(forest,dp, new_row, new_col)+1)

    return dp[r][c]
sol = -1

for r in range(n) :
    for c in range(n) :
        sol = max(sol, roaming_forest(forest, dp, r, c))

print(sol)