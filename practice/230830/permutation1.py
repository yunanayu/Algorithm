'''
0 1 2
0 2 1
1 0 2
1 2 0
2 0 1
2 1 0
'''

def perm(k):
    if k == N:
        print(bits)
        return

    for i in range(N):      # 사용여부 따지기
        if not used[i]:
            bits[k] = i     # k 번째 값에 답을 덮어쓰고 있기 때문에 원복 필요 없음
            used[i] = True
            perm(k+1)
            used[i] = False     # 다음 반복을 위해 원상복구

N = 4
# numbers = [8, 10, 20, 3]
used = [False]*N
bits = [-1] * N
perm(0)
