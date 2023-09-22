# 장훈이의 높은 선반
import sys
sys.stdin = open('input.txt','r')

def height(index,h):
    global minV
    if h >= B:
        if minV > h:
            minV = h
        return
    if index == N:
        return

    height(index+1, h+H[index])
    height(index+1, h)



T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minV = 100000
    height(0,0)
    print(f'#{tc}', abs(B-minV))


'''
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
'''