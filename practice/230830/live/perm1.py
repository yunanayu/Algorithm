# ex2

def f(i, N, card):
    if i == N:  # 순열 완성
        return
    else:
        for j in range(N):
            if used[j] == 0: # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 1
card = [1,2,3,4,5]
used = [0] *5
p = [-1]*5
