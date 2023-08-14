# 계산기1

'''
(6+5*(2-8)/2)
6528-*2/+
'''

ST = [0] * 100
top = -1
icp = {'(' : 3, '*': 2, '/': 2, '+':1, '-':1}
isp = {'(' : 0, '*': 2, '/': 2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x in '(+-*/)':
        if top == -1 or isp[ST[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
            top += 1    #push
            ST[top] = x
        elif isp[ST[top]] >= icp[x]:
            while top > -1 and isp[ST[top]] >= icp[x]:
                susik += ST[top]
                top -= 1
            top += 1
            ST[top] = x