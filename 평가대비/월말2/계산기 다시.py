import sys
sys.stdin = open("input.txt", "r")


def step1(code):
    result = []
    ST =[]
    icp = {'(':3, '+':1, '-':1, '*':2, '/': 2}
    isp = {'(':0, '+':1, '-':1, '*':2, '/': 2}
    for c in code:
        if c.isdigit():
            result.append(c)
        elif c == ')':
            while ST and ST[-1] != '(':
                v = ST.pop()
                result.append(v)
            ST.pop()
        else:
            while ST and icp[c] <= isp[ST[-1]]:
                result.append(ST.pop())
            ST.append(c)
    while ST:
        result.append(ST.pop())

    return result

def step2(result):
    ST = []
    for r in result:
        if r.isdigit():
            ST.append(int(r))
        elif r == '+':
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(v1 + v2)
        elif r == '-':
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(v2 - v1)
        elif r == '*':
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(v1 * v2)
        elif r == '/':
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(v2 // v1)
    return ST.pop()



for tc in range(1, 11):
    L = int(input())
    code = input()
    result = step1(code)
    print(step2(result))
