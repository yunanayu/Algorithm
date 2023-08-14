# 계산기2  후위표기법

'''
6528-*2/+
'''

ST = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':     # 피연산자이면
        top += 1
        ST[top] = int(x)
    else:
        op2 = ST[top]
        top -= 1
        op1 = ST[top] # pop()
        top -= 1
        if x == '+':        # op1 + op2
            top += 1
            ST[top] = op1 + op2
        elif x == '-':
            top += 1
            ST[top] = op1 - op2
        elif x == '/':
            top += 1
            ST[top] = op1 / op2
        elif x == '*':
            top += 1
            ST[top] = op1 * op2
print(ST[top])