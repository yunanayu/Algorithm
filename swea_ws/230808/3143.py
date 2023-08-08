# 가장 빠른 문자열 타이핑

T = int(input())
for t in range(1, T+1):
    A, B = (input().split())
    a = (len(A))
    b = (len(B))
    cnt = 0
    i = 0
    while i < a:
        if A[i:i+b] != B:
            cnt += 1
            i += 1
        else:
            cnt += 1
            i += b

    print(f'#{t} {cnt}')
