import sys
sys.stdin = open('input1.txt', 'r')

def cal(l,r,op):
    if op == '+':
        return l+r
    elif op == '-':
        return l-r
    elif op == '*':
        return l*r
    else:
        return l/r


def postorder(root):
    if root > N:
        return 0
    if Tree[root][0].isdecimal():
        return int(Tree[root][0])
    else:
        v1 = postorder(int(Tree[root][1]))
        v2 = postorder(int(Tree[root][2]))
        return cal(v1, v2, Tree[root][0])


for tc in range(1, 11):
    N = int(input())
    Tree = [[0,0] for _ in range(N+1)]
    for _ in range(N):
        s = list(input().split())
        Tree[int(s[0])] = s[1::]
    # print(Tree)
    print(f'#{tc} {int(postorder(1))}')
