N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
G = [[0] for _ in range(N+1)]

# cl = [0] * (N+1)
# cr = [0] * (N+1)
# pn = [0] * (N+1)  # 부모 정보 저장
# for i in range(0, len(lst), 2):
#     p = lst[i]
#     c = lst[i+1]
#     pn[c] = p
#     if cl[p] == 0:
#         cl[p] = c
#     else:
#         cr[p] = c
#
# print(pn)       # [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]     # ex) 6의 부모 노드-> 3 의 부모노드 -> 1

# # ======================================================
TREE = [[0,0,0] for _ in range(N+1)]  # 부모 자식 노드
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    if TREE[p][0] == 0:     # 왼쪽이 비어있으면
        TREE[p][0] = c
    else:
        TREE[p][1] = c

    TREE[c][2] = p  # TREE에 부모노드 정보 추가
print(TREE)

# # ================================
# for i in range(0, len(lst), 2):
#     p = lst[i]
#     c = lst[i+1]
#     G[p].append(c)
# print(G)


