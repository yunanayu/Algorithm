# 백만장자 프로젝트



#-----------------------------------------------------------
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    A = list(map(int, input().split()))
    arr = A[::-1]
    max_arr = arr[0]
    price = 0
    for i in range(1, N):
        if max_arr > arr[i]:
            price += max_arr - arr[i]
        else:
            max_arr = arr[i]

    print(fr'#{tc} {price}')
