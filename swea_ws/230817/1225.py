# [S/W 문제해결 기본] 7일차 - 암호생성기
for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    i = 1
    while data[-1] > 0:
        n = data.pop(0)
        data.append(n-i)
        i += 1
        if i == 6:
            i = 1
    if data[-1] < 0:
        data[-1] = 0
    print(f'#{tc}', *data)
