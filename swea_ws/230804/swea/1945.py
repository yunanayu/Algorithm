# 소인수분해
def cal(number, num):  # 소인수 분해 지수, 분해 후 남은 수
    cnt = 0
    while number % num == 0:
        cnt += 1
        number = number // num
    return number, cnt

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    a = cal(N, 2)
    b = cal(a[0], 3)
    c = cal(b[0], 5)
    d = cal(c[0], 7)
    e = cal(d[0], 11)
    print(f'#{tc} {a[1]} {b[1]} {c[1]} {d[1]} {e[1]}')