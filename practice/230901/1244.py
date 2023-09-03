# 최대상금 # for문 사용
import sys
sys.stdin = open('1244.txt','r')

TC = int(input())
for tc in range(1, TC+1):
    S, C = input().split()      # S 숫자판 C 교환횟수
    T = int(C)
    L = len(S)
    lst = [[] for _ in range(T+1)]
    lst[0].append(S)
    # print(lst)
    for t in range(1, T+1): # 변경횟수
        for l in lst[t-1]:
           for i in range(L-1):
               for j in range(i+1, L):
                   temp = list(l)
                   temp[i],temp[j] = temp[j],temp[i]
                   temp = ''.join(temp)
                   if temp not in lst[t]:
                       lst[t].append(temp)

    # print(lst[T])
    for i in range(len(lst[T])):
        lst[T][i] = int(lst[T][i])
    # print(lst[T])
    result = max(lst[T])
    print(f'#{tc} {result}')