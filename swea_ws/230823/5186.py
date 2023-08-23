# 이진수2
import sys
sys.stdin = open('input2.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    N = float(input())
    # print(N)
    i = -1
    cnt = 0
    result = ''
    sumV = 0
    while sumV <= N and cnt < 13:
        if sumV + 2 ** i <= N:
            sumV += 2**i
            result = result +'1'
            if sumV == N:
                break
        else:
            result = result + '0'
        i -= 1
        cnt += 1
    if cnt < 13:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc}', 'overflow')
