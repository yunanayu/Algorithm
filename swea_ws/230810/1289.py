# # 원재의 메모리 복구하기

TC = int(input())
for tc in range(1, TC+1):
    M = list(map(int, input()))
    bit = [0] * len(M)
    cnt = 0
    for i in range(len(M)):
        if M[i] != bit[i]:
            cnt += 1
            for j in range(i, len(M)):
                bit[j] = M[i]

    print(f'#{tc} {cnt}')

