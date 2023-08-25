# 보물상자 비밀번호
import sys
sys.stdin = open('5658.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    S = input()
    L = len(S)//4
    lst = []
    for idx in range(0, N, L):
        t = int(S[idx:idx+L], 16)
        lst.append(t)

    print(lst)
    #
    # s_lst = []
    # for i in range(0, L, 3):
    #     s_lst.append(S[i:i+3])
    # print(s_lst)
