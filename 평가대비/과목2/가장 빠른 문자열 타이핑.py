TC = int(input())
for tc in range(1, TC+1):
    txt, patt = input().split()

    t = len(txt)
    p = len(patt)

    tp = 0
    pp = 0
    cnt = 0
    while tp < t and pp < p:
        if txt[tp] != patt[pp]:
            tp = tp - pp + 1
            pp = 0
        else:
            tp += 1
            pp += 1

        if pp == p:
            cnt += 1
            pp = 0

    print(f'#{tc} {t - p * cnt + cnt}')