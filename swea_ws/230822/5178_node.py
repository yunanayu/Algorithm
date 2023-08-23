import sys
sys.stdin = open('input3.txt', 'r')

def postorder(root):
    if root > N:
        return 0
    if Tree[root]:
        return Tree[root]
    v1 = postorder(root*2)
    v2 = postorder(root*2 + 1)
    Tree[root] = v1+v2
    return Tree[root]


TC = int(input())
for tc in range(1, TC+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    # print(arr)
    Tree = [0] * (N+1)
    for i in range(M):
        Tree[arr[i][0]] = arr[i][1]
    print(f'#{tc} {postorder(L)}')


#----------------------------------------------------------------------------
for i in range(N, 0, -1):
    Tree[i//2] += Tree[i]