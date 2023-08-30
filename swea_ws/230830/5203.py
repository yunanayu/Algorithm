# 베이비진
import sys
sys.stdin = open('5203.txt','r')

def baby_gin(lst):
    cnta = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] == lst(j):
                cnta += 1
            if cnta >= 2:
                return 'triplet'
    for l in lst:
        key = l
        i = 1



TC = int(input())
for tc in range(1, TC+1):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    A = []
    B = []
    for i in range(0,N-1,2):
        A.append(num_list[i])
        B.append(num_list[i+1])
