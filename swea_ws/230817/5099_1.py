# 피자 굽기

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    pans = [0] * N
    newpizza = 1
    while pans:
        pizzaNo = pans.pop(0)
        C[pizzaNo] //= 2
        if C[pizzaNo] == 0:
            if newpizza <= M:
                pans.append(newpizza)
                newpizza += 1
        else:
            pans.append(pizzaNo)

    print(pizzaNo)