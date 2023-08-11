T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    stick_cnt = 0
    result = 0
    for c in range(len(lst)):
        if lst[c] == '(':
            if lst[c+1] == ')' :
                result += stick_cnt
            else:
                stick_cnt +=1
        else:
            if lst[c-1] != '(' :
                result += 1
                stick_cnt -= 1
        # elif ')':
    print(f'#{tc}', result)