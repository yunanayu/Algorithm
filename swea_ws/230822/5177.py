import sys
sys.stdin = open('input2.txt', 'r')

def cal(p):
    global sumV
    if p == 1:
        return sumV
    else:
        sumV += Tree[p//2]
        return cal(p//2)

def insert(key):
    global last
    last += 1
    Tree[last] = key
    c = last
    p = c // 2
    while p>0:
        if Tree[p] > Tree[c]:
            Tree[p], Tree[c] = Tree[c], Tree[p]
            c = p
            p = c//2
        else:
            return

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    Tree = [0] * (N+1)
    last = 0
    for i in lst:
        insert(i)
    sumV = 0
    # print(Tree)
    print(f'#{tc} {cal(N)}')
