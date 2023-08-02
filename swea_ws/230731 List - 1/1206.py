TC = 10
for tc in range(1, TC+1):
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if H[i] > H[i-2] and H[i] > H[i + 2] and H[i] > H[i+1] and H[i] > H[i-1]:
            a = H[i]-H[i-2]
            b = H[i]-H[i+2]
            c = H[i]-H[i-1]
            d = H[i]-H[i+1]
            m = min(a, b, c, d)
            cnt = cnt + m
    print(f'#{tc} {cnt}')


#1 691
#2 9092
#3 8998
#4 9597
#5 8757
#6 10008
#7 10194
#8 10188
#9 9940
#10 8684
# 3 5 2 4 9 0 6 4 0 6