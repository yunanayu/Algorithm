# 이진탐색
def inorder(root):
    global num
    if root <= N:
        inorder(root*2)
        Tree[root] = num
        num += 1
        inorder(root*2+1)
    return Tree

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    Tree = [[] for _ in range(N + 1)]
    num = 1
    result = inorder(1)
    print(f'#{tc} {result[1]} {result[N//2]}')