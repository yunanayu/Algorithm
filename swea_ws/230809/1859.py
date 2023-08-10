# 백만장자 프로젝트

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ST = []
    price = 0
    for n in arr:
        if not ST or ST[-1] <= n:
            ST.append(n)
        else:
            s = len(ST)
            for i in range(s-1):
                price += ST[i]
            price = (s-1) * ST[s-1] - price
            ST = []
            ST.append(n)
    s = len(ST)
    for i in range(s - 1):
        price += ST[i]
    price = (s - 1) * ST[s - 1] - price

    print(price)