TC = 10
for tc in range(1, TC+1):
    n, a = input().split()
    N = int(n)
    arr = list(a)
    ST = []
    for a in arr:
        if not ST or ST[-1] != a:
            ST.append(a)
        else:
            ST.pop()
    print(''.join(ST))