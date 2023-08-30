a = [3,6,7,1,5,4]
N = 6
for i in range(1, (1<<N)-1):    # 공집합 제외, 끝 값(=[]) 제외
    subset1 = []
    subset2 = []
    for j in range(N):
        if i&(1<<j):     # j번 비트가 0이 아니면
            subset1.append(a[j])
        else:
            subset2.append(a[j])
    print(subset1, subset2)