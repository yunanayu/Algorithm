def pre_order(root):
    if root:
        print(root)
        pre_order(TREE[root][0])  # 왼쪽
        pre_order(TREE[root][1])  # 오른쪽

N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
G = [[0] for _ in range(N + 1)]

TREE = [[0, 0, 0] for _ in range(N + 1)]  # 부모 자식 노드
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i + 1]
    if TREE[p][0] == 0:  # 왼쪽이 비어있으면
        TREE[p][0] = c
    else:
        TREE[p][1] = c

    TREE[c][2] = p  # TREE에 부모노드 정보 추가
# print(TREE)