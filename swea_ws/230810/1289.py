# 원재의 메모리 복구하기
TC = int(input())
for tc in range(1, TC+1):
    M = list(map(str, input()))
    m = len(M)
    # print(M)
    cnt = 0
    arr = [0] * m
    for i in range(m):
        if M[i] == '1':
            for j in range(i,m