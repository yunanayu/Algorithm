# 괄호를 확인하여 이상이 있으면 False
# 없으면 True 를 return

def check(s):   # 괄호쳌
    pass
def cal(s):
    ST = []
    for c in s:
        if c == ')':
            tmp = 0
            while ST and ST[-1] != '(':
                tmp += int(ST.pop())
            if ST:
                ST.pop()
                ST.append(tmp)
            else:
                return -1

        elif c =='}':
            tmp = 1
            while ST and ST[-1] != '{':
                tmp += int(ST.pop())
            if ST:
                ST.pop()
                ST.append(tmp)
            else:
                return -1
        else:
            ST.append(c)

    if len(ST) == 1:
        return ST.pop()
    else:
        return -1

# 게산ㅇ을 수행한 결과를 return
def cal(s):
    ST = []
    for c in s:
        if c == ')':
            tmp = 0
            while ST and ST[-1] != '(':
                tmp += int(ST.pop())
            if ST[-1]