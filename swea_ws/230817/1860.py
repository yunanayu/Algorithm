import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())     # N: 사람 수/ M: 붕어빵 만드는 시간/ K: 만들 수 있는 붕어빵 개수
    time = list(map(int, input().split()))  # 손님 도착 시간
