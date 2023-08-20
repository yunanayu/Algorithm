import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(arr)

    # 행우선
    for r in range(N):
        for c in range(M):
