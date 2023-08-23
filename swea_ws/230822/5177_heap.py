import sys
sys.stdin = open('input2.txt', 'r')
#
# def insert(key):
#     global Tree
#     global last
#     Tree[last] =
#     pass

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    TREE = [0] + list(map(int, input().split())) + [0]*100
    # no = 0
    # Tree = [[no,0]]
    # for i in lst:
    #     no += 1
    #     Tree = Tree + [[no,i]]
    # Tree = [0]
    # for i in range(1, N):
    #     Tree = Tree + [0]
    #
    # print(Tree)
    #     last = i
    print(TREE)