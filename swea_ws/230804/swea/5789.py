# 현주의 상자 바꾸기
TC = int(input())
for tc in range(1, TC+1):
    N, Q = map(int, input().split()) # N: 상자의 개수 Q: 번호 변경 횟수
    box = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for n in range(L-1, R):
            box[n] = i
    print(f'#{tc}', *box)