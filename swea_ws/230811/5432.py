# 쇠막대기 자르기

TC = int(input())
for tc in range(1, TC+1):
    lst = input()
    cnt = 0
    result = 0
    for i in range(len(lst)):
        if lst[i] == '(':
            if lst[i+1] == ')':
                result += cnt
            else:
                cnt += 1
        else:
            if lst[i-1] == ')':
                result += 1
                cnt -= 1

    print(f'#{tc} {result}')
