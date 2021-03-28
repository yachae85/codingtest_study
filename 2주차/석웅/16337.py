from itertools import combinations

def insert_operator(compute_graph, operator_id) :
    if len(compute_graph.keys()) == 0 :
        compute_graph[1] = operator_id
        return
    cur = 1
    while True :
       if compute_graph[cur] > operator_id :
           cur = 2*cur
       else :
           cur = 2*cur + 1

       if cur not in compute_graph.keys() :
           compute_graph[cur] = operator_id
           break

    return

def make_compute_graph(operators) :
    compute_graph = dict()
    for operator in operators :
        insert_operator(compute_graph,operator)

    return compute_graph

def compute_one_operator(operator, operand1, operand2) :
    if operator == '+' :
        return operand1 + operand2
    if operator == '-' :
        return operand1 - operand2
    if operator == '*' :
        return operand1 * operand2
    return

def compute_expression(compute_graph, expression, cur) :
    if cur not in compute_graph.keys() :
        operator = compute_graph[cur//2]
        return int(expression[operator + (-1)**(cur%2+1)])

    left_val = compute_expression(compute_graph, expression, 2*cur)
    operator = compute_graph[cur]
    right_val = compute_expression(compute_graph, expression, 2*cur+1)

    return compute_one_operator(expression[operator], left_val, right_val)



N = int(input())
expression = input()


operators = [  operator_id for operator_id in range(1,len(expression),2)]


combs = list()
for i in range(len(operators)) :
    combs.extend(combinations(operators,i))

compute_graph = None
max_result = -(2**31)
for comb in combs :
    comb = list(comb)
    flag = False
    for i in range(len(comb)-1) :
        if abs(comb[i]-comb[i+1]) == 2 :
            flag =True
            break
    if flag : continue
    comb = comb + [operator_id for operator_id in operators if operator_id not in comb]
    comb.reverse()
    compute_graph = make_compute_graph(comb)
    result = compute_expression(compute_graph, expression, 1)
    if max_result < result :
        max_result = result

if N == 1 :
    print(expression[0])
else :
    print(max_result)