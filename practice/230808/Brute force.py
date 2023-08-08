# t 안에서 p 가 존재하면 위치를 return 못찾으면 -1 return
def brute(t, p):
    N = len(t)
    M = len(p)

    tp = 0  # text 의 위치
    pp = 0  # patt 의 위치
    while tp < N and pp < M:    # 찾으면 후자 못찾으면 전자의 조건으로 반복문 빠져나옴
        if t[tp] != p[pp]:
            tp = tp - pp + 1    # 시작위치로 돌아 간 후 그 다음으로 이동
            pp = 0
        else:
            tp += 1
            pp += 1
        '''
        if t[tp] != p[pp]:
            tp = tp - pp  # 시작위치로 돌아 간 후 그 다음으로 이동
            pp = -1
        tp += 1
        pp += 1
        '''

    if pp == M:
        return tp-M     # 시작위치
    else:
        return -1



text = 'TTTTAACCA'
patt = 'TTA'
print(brute(text, patt))