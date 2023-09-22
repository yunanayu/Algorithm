# 수영장
import sys
sys.stdin = open('input.txt','r')

def swim():
    global ans
    if ans ==


T = int(input())
for tc in range(1, T+1):
    D, M, T, Y = map(int, input().split())
    S = [0] + list(map(int, input().split()))
    ans = 100000000000
