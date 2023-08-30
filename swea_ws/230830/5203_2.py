# 베이비진
import sys
sys.stdin = open('5203.txt','r')


def baby_gin(lst):
    lst = sorted(lst)
    for i in range(len(lst)-2):
        cnt_a = 0
        cnt_b = 0
        n =1
        for j in range(i,len(lst)):
            if lst[i] == lst[j]:
                cnt_a += 1
            elif lst[i] == lst[j] - n:
                cnt_b += 1
                n += 1
            if cnt_a >= 2:
                return 'a'
            elif cnt_b >= 2:
                return 'b'
    return 0

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
        x = baby_gin(A)
        y = baby_gin(B)
        if i >= 5:
            if x == 'a' or x == 'b' and y == 0:
                print(1)
                break
            elif y == 'a' or y == 'b' and x == 0:
                print(2)
                break
            elif x == 0 and y == 0:
                continue
    if x == 0 and y == 0:
        print(0)
