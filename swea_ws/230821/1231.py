# 중위순회
import sys
sys.stdin = open('input.txt', 'r')

# def inorder(root):
#     global result
#     if root <= N:
#         inorder(root*2)
#         result = result + Tree[root][0]
#         inorder(root*2+1)
#     return result
#
#
# # for tc in range(1, 11):
# #     N = int(input())
# #     Tree = [[] for _ in range(N+1)]
# #     for _ in range(N):
# #         s = input().split()
# #         no = int(s[0])
# #         Tree[no] = s[1::]
# #     # print(Tree)
# #     result = ''
# #     print(f'#{tc} {inorder(1)}')
#
#
# for tc in range(1,11):
#     N = int(input())
#     Tree = [[] for _ in range(N+1)]
#     for _ in range(N):
#         S = list(input().split())
#         no = int(S.pop(0))
#         Tree[no] = S[0]
#     # print(Tree)
#     result = ''
#     print(f'#{tc} {inorder(1)}')

def inorder(root):
    global result
    if root <= N:
        inorder(root*2)
        result = result + Tree[root]
        inorder(root*2+1)
    return result


for tc in range(1,11):
    N = int(input())
    Tree = [[] for _ in range(N+1)]
    for _ in range(N):
        S = list(input().split())
        no = int(S[0])
        Tree[no] = S[1]
    # print(Tree)
    result = ''
    print(f'#{tc} {inorder(1)}')