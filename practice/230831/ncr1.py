def subset(k):
    if k == K:
        print(bits)
        return
    bits[k] = 0
    subset(k+1)

    bits[k] = 1
    subset(k+1)



def perm(k):
    if k == N:
        print(bits)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            bits[k] = i
            perm(k+1)
            used[i] = False

def perm2(k):
    if k == K2:
        print(bits)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            bits[k] = i
            perm(k+1)
            used[i] = False


N = 5
K = 3
K2 = 3
bits = [-1] * K
used = [False] * N
subset(0)
# perm(0)
# perm2(0)
