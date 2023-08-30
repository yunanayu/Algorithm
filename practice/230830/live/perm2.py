def f(i, N):# i 이전에 고른 개ㅜㅅ= zN개에서  K 개를 골느는 수열
    if i == N:  # 순열 완성
        print(cnt, p)
        return
    else:   # p[i] 에 들
        for j in range(N):
            if used[j] == 0:# 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 1
card = [1,2,3,4,5]
N = 5
K = 3
used = [0] *5   # 이미 사용한 카드인지 확인
p = [0] * 2
cnt =0
f(0,5)