def comb(k, s):
    if k== K:
        print(result)
        return
    for i in range(s, N):   #N -> N-K+1+k
        result[k] = i
        comb(k+1, i+1)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
N = 4
visited = [False] * N
K = 3 #depth
result = [-1] * K
comb(0, 0)