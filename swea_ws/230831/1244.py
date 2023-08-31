# 최대상금
import sys
sys.stdin = open('1244.txt','r')

def solve(k,s):
    global maxV
    if k == cnt:
        if maxV < int(s):
            maxV = int(s)
        return
    if s in memo[k]:
        return
    else:
        memo[k].append(s)

    templst = list(s)
    for i in range(N-1):
        for j in range(i+1, N):
            templst[i], templst[j] = templst[j], templst[i]
            solve(k+1, ''.join(templst))
            templst[i], templst[j] = templst[j], templst[i]


TC = int(input())
for tc in range(1, TC+1):
    s, c = input().split()
    cnt = int(c)
    maxV = 0
    N = len(s)
    memo = [[] for _ in range(cnt)]
    solve(0,s)
    print(f'#{tc} {maxV}')