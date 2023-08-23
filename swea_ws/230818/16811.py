'''
lst = [1, 2, 3, 4, 5, 6, 7, 8]

N = 8
S,M을 구분짓는 경계 =>
a 범위는 0 ~ N-3 S = [0:a+1]

M, L 을 구분짓는 경계 =>

original = [1, 2, 2, 2, 5, 6, 7, 8]
counts = [0] * 50
for v in original:
    counts[v] += 1

counts =

'''
# 당근 포장하기
import sys
sys.stdin = open("input.txt", "r")



TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    # print(Ci)
    counts = [0] * 1001
    for c in Ci:
        counts[c] += 1
    # print(counts)

    minV = min(Ci)
    maxV = max(Ci)
    result = N

    for a in range(minV, maxV-1):
        for b in range(a+1, maxV):
            S = sum(counts[minV:a+1])
            M = sum(counts[a+1:b+1])
            L = sum(counts[b+1:maxV+1])

            if S == 0 or M == 0 or L == 0:  # 하나라도 빈곳이 있으면:
                continue
            if S > N//2 or M > N//2 or L > N//2: # 하나라도 N//2 보다 큰것이 있으면:
                continue

            d =  max(S,M,L) - min(S,M,L)
            if result > d:
                result = d

    if result == N:
        result = -1
    print(f'#{tc} {result}')