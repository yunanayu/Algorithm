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
    if Tree[root].isdecimal():
        return int(Tree[root])
    else:
        v1 = postorder(root*2)
        v2 = postorder(root*2+1)
        return cal(int(v1), int(v2), Tree[root])

for tc in range(1, 11):
    N = int(input())
    Tree = [0] * (N+1)
    for _ in range(N):
        s = list(input().split())
        if s[1] in ['+','-','/','*']:
            Tree[int(s[0])] = s[1]
        else:
            Tree[int(s[0])] = s[1]
    print(Tree)
    print(postorder(1))
