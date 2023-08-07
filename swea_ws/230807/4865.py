TC = int(input())
for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    cnt_max = 0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
        if cnt_max < cnt:
            cnt_max = cnt
    print(f'#{tc} {cnt_max}')














