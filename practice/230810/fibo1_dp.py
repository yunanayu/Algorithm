def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


cnt = 0 # 함수가 호출되는 횟수
print(fibo(30), cnt)
