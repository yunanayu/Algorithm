# if icp[ST[-1]] < icp[c]:
#     ST.append(c)
# else:
#     v = ST.pop()
#     result.append(v)
#     ST.append(c)

s = '(6+5*(2-8)/2)'

def STEP1():
    result = []
    ST = []
    icp = {'(':3, '+':1, '-':1, '*':2, '/':2}
    isp = {'(':0, '+':1, '-':1, '*':2, '/':2}
    for c in s:
        if c.isdigit():
            result.append(c)
        # elif c == '(':
        elif c == ')':
            while ST and ST[-1] != '(':
                v = ST.pop()
                result.append(v)
            ST.pop()
        else:
            if ST and isp[ST[-1]] >= icp[c]:
                v = ST.pop()
                result.append(v)
            ST.append(c)
    while ST:
        v = ST.pop()
        result.append(v)
    return result

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    if op == '-':
        return v2 - v1
    if op == '*':
        return v1 * v2
    if op == '/':
        return v2 // v1

def STEP2(s):
    ST = []
    for c in s:
        if c.isdigit():
            ST.append(c)
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(cal(int(v1), int(v2), c))
    return ST.pop()



step1_s = STEP1()   # 중위표현을 후위표현으로 변경
print(step1_s)
result = STEP2(step1_s)
print(result)

