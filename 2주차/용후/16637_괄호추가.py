import sys

n = int(input())
exp = input()
result = -sys.maxsize


def help(x, y, op):
    a = int(x)
    b = int(y)
    if op == '+':
        return str(a+b)
    elif op == '-':
        return str(a-b)
    else:
        return str(a * b)


def calc(comb):
    e = []
    i = 0
    while i < n:
        if exp[i].isdigit():
            e.append(exp[i])
            i += 1
        else:
            if i in comb:
                e.append(help(e.pop(), exp[i+1], exp[i]))
                i += 2
            else:
                e.append(exp[i])
                i += 1

    result = 0
    i = 0
    num = []
    while i < len(e):
        if e[i] not in "+*-":
            num.append(e[i])
            i += 1
        else:
            num.append(help(num.pop(), e[i+1], e[i]))
            i += 2
    return int(num[0])


def dfs(start, comb):
    global result
    if start > len(exp)-2:
        return

    for i in range(start, len(exp), 2):
        comb.append(i)
        result = max(result, calc(comb))
        dfs(i+4, comb)
        comb.pop()


if n == 1:
    print(int(exp[0]))
else:
    dfs(1, [])
    print(result)
