# [S/W 문제해결 기본] 10일차 - 비밀번호


for tc in range(1, 11):
    n, arr = input().split()
    N = int(n)
    arr = list(arr)
    # arr = list(str(arr))
    ST = []
    for n in arr:
        if not ST or ST[-1] != n:
            ST.append(n)
        else:
            ST.pop()
    print(f'#{tc}', ''.join(ST))