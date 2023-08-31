import sys
sys.stdin = open('5203.txt','r')

def b(lst):
    global result
    i = 0
    while i <= (len(lst) - 1):
        if lst[i] >= 3:
            result = 1
            return
        if i <= (len(lst) - 3):
            if lst[i] != 0 and lst[i + 1] != 0 and lst[i + 2] != 0:
                result = 1
                return
        i += 1
    return


TC = int(input())
for tc in range(1, TC + 1):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    counts_A = [0] * 10
    counts_B = [0] * 10
    result = 0
    for i in range(0, N - 1, 2):
        counts_A[num_list[i]] += 1
        counts_B[num_list[i + 1]] += 1
        if i >= 6:
            b(counts_A)
            if result == 1:
                print(f'#{tc}', 1)
                break
            b(counts_B)
            if result == 1:
                print(f'#{tc}', 2)
                break

    if result == 0:
        print(f'#{tc}', 0)