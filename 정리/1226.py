# [S/W 문제해결 기본] 7일차 - 미로1
import sys
sys.stdin = open('input.txt', 'r')

def find(sr, sc):
    visited = [[False] * 16 for _ in range(16)]




for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
