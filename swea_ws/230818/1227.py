# 미로
import sys
sys.stdin = open("input.txt", "r")


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    print(arr)