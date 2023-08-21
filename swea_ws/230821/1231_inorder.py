def inorder(root):
    if root > N :
        return

    inorder(root*2)
    arr[root] = value
    value += 1
    inorder(root*2+1)

     =====================

    if root <= N:
        inorder(root * 2)
        arr[root] = value
        value += 1
        inorder(root * 2 + 1)



N = int(input())
Tree = [[] for _ in range(N+1)]

for _ in range(N):
    s = input().split()
    no = int(s[0])
    Tree[no] = s[1::]
print(Tree)