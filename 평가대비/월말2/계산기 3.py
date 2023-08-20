import sys
sys.stdin = open("input.txt", "r")

def step1(code):
    result = []
    ST = []
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
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
    for i in result:
        if i.isdigit():
            ST.append(int(i))
        elif i == '+':
            v1= ST.pop()
            v2 = ST.pop()
            ST.append(v1 + v2)
        elif i == '-':
            v1= ST.pop()
            v2 = ST.pop()
            ST.append(v2-v1)
        elif i == '*':
            v1= ST.pop()
            v2 = ST.pop()
            ST.append(v1 * v2)
        elif i == '/':
            v1= ST.pop()
            v2 = ST.pop()
            ST.append(v2 // v1)
    return ST.pop()




for i in range(1,11):
    tc = int(input())
    case = input()
    print(f'#{i} {step2(step1(case))}')
