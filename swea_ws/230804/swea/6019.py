# 기차 사이의 파리
TC = int(input())
for tc in range(1, TC+1):
    D, A, B, F = map(int, input().split())
    s = F * D /(A + B)
    print(f'#{tc} {s}')