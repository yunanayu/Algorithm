s = '(6+5*(2-8)/2)'

value = []
ST = []

icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for i in s:
    if i.isdigit():
        value.append(i)
    elif i == ')':
        while ST[-1] != '(':
            v = ST.pop()
            value.append(v)
        ST.pop()
    else:
        if ST and isp[ST[-1]] < icp[i]:
            ST.append(i)

print(value)

