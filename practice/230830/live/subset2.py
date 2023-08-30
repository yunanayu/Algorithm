a = [1,2,3,4]
N = len(a)
# for i in range(1, 1<<(N-1)): # 위 아래 같은 결과
for i in range(1, (1<<N)//2):  # 전체 16개 중 7개 값만 나옴  # 공집합 제외, 끝 값(=[]) 제외
    subset1 = []
    subset2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j):     # j번 비트가 0이 아니면
            subset1.append(a[j])
            total1 += a[j]
        else:
            subset2.append(a[j])
            total2 += a[j]

    r1 = f(subset1)
    r2 = f(subset2)
    if r1 and r2:
        if min_v>abs(total1-total2):
    # print(subset1, subset2)