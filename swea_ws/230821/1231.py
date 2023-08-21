# 중위순회
import sys
sys.stdin = open('input.txt', 'r')

def inorder(root):
    global result
    if root <= N:
        inorder(root*2)
        result = result + Tree[root][0]
        inorder(root*2+1)
    return result


for tc in range(1, 11):
    N = int(input())
    Tree = [[] for _ in range(N+1)]
    for _ in range(N):
        s = input().split()
        no = int(s[0])
        Tree[no] = s[1::]
    # print(Tree)
    result = ''
    print(f'#{tc} {inorder(1)}')