# 피보나치 수열 재귀함수
def fib(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1      # 종료조건 1
    if n <= 1:
        return n      # 종료조건 2

    v1 = fib(n-1)
    v2 = fib(n-2)

    return v1 + v2

N = 5
print(fib(5))

## memoization   # 효율을 향상시키기 위해 사용

def fib(n):
    if memo[n] != -1:     #이미 알고 있는지
        return memo[n]    #알고 있는 값      # memoization 사용시 필요한 조건

    if n <= 1:
        memo[n] = n
        return n  # 종료조건 2

    v1 = fib(n - 1)
    v2 = fib(n - 2)
    memo[n] = v1 + v2
    return memo[n]


N = 5
memo = [-1] * (N + 1)  # N개 생성
# memo[0] = 0
# memo[1] =[1] # 사용시 종료조건 2 필요 없음
print(fib(5))

