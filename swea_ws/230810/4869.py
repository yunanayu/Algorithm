# 종이 붙이기
def fibo(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]
    return dp[n]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    n = N // 10

    print(f'#{tc} {fibo(n)}')
