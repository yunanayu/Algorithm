import sys
sys.stdin = open("input.txt", "r")

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Ci = list(map(int, input().split()))
