# Forth

import sys
sys.stdin = open('input.txt','r')


def cal(code):
    ST = []
    for c in code:
        if c.isdecimal():
            ST.append(int(c))
        else:
            if ST and c in '*/+-':
                if len(ST) < 2:
                    return 'error'
                elif c == '+':
                    v1 = ST.pop()
                    v2 = ST.pop()
                    ST.append(v1 + v2)
                elif c == '-':
                    v1 = ST.pop()
                    v2 = ST.pop()
                    ST.append(v2 - v1)
                elif c == '*':
                    v1 = ST.pop()
                    v2 = ST.pop()
                    ST.append(v1 * v2)
                elif c == '/':
                    v1 = ST.pop()
                    v2 = ST.pop()
                    ST.append(v2 // v1)
            elif c == '.':
                if len(ST)> 1:
                    return 'error'
                else:
                    return ST.pop()

TC = int(input())
for tc in range(1, TC+1):
    code = list(input().split())
    print(f'#{tc} {cal(code)}')

    #
    # if not ST:
    #     print(f'#{tc}', 'error')