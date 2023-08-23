import sys
sys.stdin = open('input1.txt', 'r')


def postorder(root):
    if Tree[root].isdigit():
        return Tree[root]
    else:
        v1 = postorder(root*2)
        v2 = postorder(root*2+1)
        return cal(v1, v2, Tree[root])


def cal(v1,v2,s):
    if s == '+':
       return v1 + v2
    elif s == '*':
        return  v1 * v2
    elif s == '-':
        return  v1 - v2
    elif s == '/':
        return  v1 // v2


for tc in range(1, 11):
    N = int(input())
    Tree = [0] * (N+1)
    for _ in range(N):
        s = list(input().split())
        if s[1] in ['+','-','/','*']:
            Tree[int(s[0])] = s[1]
        else:
            Tree[int(s[0])] = int(s[1])
    print(Tree)
    print(postorder(1))

'''
#1 13
#2 20
#3 35
#4 107mmmmm
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2

'''