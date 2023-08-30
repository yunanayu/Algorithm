# 베이비진
import sys
sys.stdin = open('5203.txt','r')

def perm(k):
    if k == N:
        # print(bits)
        lst = []
        for i in range(N):
            pos = bits[i]
            lst.append(A[pos])
        print(lst)
        return


    for i in range(N):      # 사용여부 따지기
        if not used[i]:
            bits[k] = i     # k 번째 값에 답을 덮어쓰고 있기 때문에 원복 필요 없음
            used[i] = True
            perm(k+1)
            used[i] = False     # 다음 반복을 위해 원상복구


def f(i, N, card):
    if i == N:  # 순열 완성
        return
    else:
        for j in range(N):
            if used[j] == 0 # 아직 사용되기 전이면
                P[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 1
card = list(map(int, input()))
used = [0] *6#


def baby_gin(lst):



TC = int(input())
for tc in range(1, TC+1):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    used = [False] * N
    bits = [-1] * N
    A = []
    B = []
    for i in range(0,N-1,2):
        A.append(num_list[i])
        B.append(num_list[i+1])
    perm(0)
