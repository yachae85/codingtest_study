import sys

# 입력 받기
N, K = map(int,sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))


#구간 구하기
dist = [(K,i) for i in range(K)]
for i in range(K) :
    for j in range(i+1,K):
        if order[i] == order[j] :
            dist[i] = (j-i,i)
            break
dist.sort()
concur_cnt = 0

print(dist)
def is_overlap(a, b):
    if a[0] < b[1] and a[1] > b[0]: return True
    return False

# searched = 해당 인덱스의 구간과 겹치는 구간들의 리스트들의 딕셔너리
# key = 현재 탐색 대상이 되는 구간의 인덱스
def overlap_search(searched, key, flags):
    if len(searched[key[0]]) == 0 : return []

    ret_list = []
    for next_st, next_ds in searched[key[0]] :
        if flags[next_ds] == False : continue
        cur_list = overlap_search(searched, (next_st, next_ds), flags)
        sch_list = [(next_st,next_ds)]
        for sch_st, sch_ds in cur_list :
            if is_overlap(key, (sch_st, sch_ds)) and ((sch_st, sch_ds) not in sch_list) and flags[sch_ds]:
                sch_list.append((sch_st,sch_ds))
        if len(ret_list) < len(sch_list) :
            print(key, sch_list)
            ret_list = sch_list


    return ret_list

dupl_dict = { k : None for k in range(K)}
cnt = 0
flags = [False for i in range(K)]
#겹치는 횟수 구하기
for i in range(K) :
    # 현재 구간 구하기
    cur_st = dist[i][1]; cur_ds = dist[i][0] + dist[i][1]
    cur_sch = set(order[:(cur_st+1)])
    if len(cur_sch) <= N :
        flags[cur_st] = True
    #if cur_st < N :
    #    flags[cur_st] = True
    # 구간이 범위를 넘어선 경우 종료
    #if cur_ds >= K : continue


    # 현재 구간보다 길이가 짧으면서 겹치도록 선택된 구간들 구하기 - 재귀적으로 풀기
    cur_dupl = list()
    for j in range(0,i) :
        sch_st = dist[j][1]; sch_ds = dist[j][0] + dist[j][1]
        if flags[sch_ds] == False : continue
        if sch_st < cur_ds and sch_ds > cur_st :
            cur_dupl.append((sch_st, sch_ds))
    dupl_dict[cur_st] = cur_dupl
    cur_list = overlap_search(dupl_dict, (cur_st,cur_ds), flags)

    other_set = set(order[cur_st+1:cur_ds])
    span_set = set([order[cur_st] for cur_st,cur_ds in cur_list])
    other_set = other_set - span_set
    #print(i, cur_list, cur_dupl)
    if len(cur_list) + 1 <= N :
        print(cur_st, cur_ds, cur_list, cur_dupl)
        print(flags)
        flags[cur_ds] = True
    else :
        flags[cur_ds] = False
    #print(flags)
print(flags)
for i in range(K) :
    cur_st = dist[i][1] ; cur_ds = dist[i][0] + dist[i][1]
    cur_sch = set(order[:(cur_st+1)])
    if len(cur_sch) <= N : continue
    if dist[i][0] == 0 and (order[cur_st] not in order[:cur_st]) :
        flags[cur_st] = False
print(flags)
print(K-sum(flags))











