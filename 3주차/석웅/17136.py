paper_size = [1,2,3,4,5]
paper_resid = [5,5,5,5,5]


ten_paper = list()


for i in range(10) :
    cur_row = input().split()
    cur_row = [int(cur_ele) for cur_ele in cur_row]
    ten_paper.append(cur_row)

def check_put_down_possible(ten_paper, st_r, st_c, size) :
    if (st_r+size) > 10 or (st_c+size) > 10 : return False
    for r in range(st_r, st_r+size) :
        for c in range(st_c, st_c+size) :
            if ten_paper[r][c] == 0 :
                return False
    return True

def tog_one_paper_down(ten_paper, st_r, st_c, size) :
    for r in range(st_r,st_r+size) :
        for c in range(st_c,st_c+size) :
            ten_paper[r][c] = 1 - ten_paper[r][c]


def put_papers_down(ten_paper, cur_r, cur_c) :

    new_r = -1; new_c = -1
    ## 시작 위치 찾기
    for r in range(10) :
        flag = False
        for c in range(10) :
            if ten_paper[r][c] == 1 :
                new_r = r
                new_c = c
                flag = True
                break
        if flag : break

    if new_r==-1 and new_c==-1 : return 0
    ret = -1

    for i in range(len(paper_resid)) :
      if paper_resid[i] < 1 : continue
      if check_put_down_possible(ten_paper, new_r, new_c, i+1) == False : continue
      paper_resid[i] -= 1
      tog_one_paper_down(ten_paper,new_r,new_c, i+1)
      new_ret = put_papers_down(ten_paper,new_r,new_c) + 1
      if new_ret>0 and (ret==-1 or ret > new_ret):
        ret = new_ret
      tog_one_paper_down(ten_paper,new_r,new_c, i+1)
      paper_resid[i] += 1

    return ret


print(put_papers_down(ten_paper,0,0))