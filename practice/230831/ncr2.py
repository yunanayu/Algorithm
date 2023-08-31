def comb(k,s):
    if k == K :
        print(bits)
        return
    for i in range(s, N-K+1+k): # = range(s, N) -> 시간초과 날 수 있음
        bits[k] = i
        comb(k+1, i+1)

N = 5
K = 3       # NCK
bits = [-1] * K
used = [False] * N
comb(0,0)