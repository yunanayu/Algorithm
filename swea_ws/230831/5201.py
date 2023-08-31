# 컨테이너 운반
import sys
sys.stdin = open('5201.txt','r')

TC= int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())        # N : 컨테이너 수, M: 트럭 수
    W = list(map(int, input().split()))     # N개의 화물의 무게
    T = list(map(int, input().split()))     # M개 트럭의 적재용량
    W.sort()
    T.sort()
    W.reverse()         # 화물 무게 무거운 순으로 정렬
    T.reverse()         # 트럭 적재용량 큰 순으로 정렬
    lst = []
    j = 0
    for i in range(N):
        if j > M-1:
            break
        if W[i] <= T[j]:
            lst.append(W[i])
            j += 1

    print(f'#{tc} {sum(lst)}')
