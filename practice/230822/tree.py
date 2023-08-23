# 이진 탐색 트리 - 연산
# 키가 있는 위치를 return 없으면 -1 을 return
def find(key):
    pos = 1
    while Tree[pos] != 0:   # 더이상 노드가 없을 때
        if Tree[pos] == key:
            return pos
        if Tree[pos] < key:
            pos = pos*2 +1
        else:
            pos = pos*2
    return -1
# 입력이 가능하면 입력 후 position return
# 이미 있어서 입력이 불가능 한 경우 -1 return
def insert(key):
    pos = 1
    while Tree[pos] != 0:  # 더이상 노드가 없을 때
        if Tree[pos] == key:
            return -1
        if Tree[pos] < key:
            pos = pos * 2 + 1
        else:
            pos = pos * 2
    Tree[pos] = key
    return pos

# 비어있는 Tree 입력으로 받기
Tree = [0] * 100

insert(9)
print(Tree)
insert(5)
print(Tree)
insert(7)
print(Tree)
insert(4)
print(Tree)
# Tree = [0, 9, 4, 12, 3, 6, 0, 15, 0, 0, 0, 0, 0, 0, 13, 17]
# Tree = Tree + [0] * 100
#
# print(find(13))
# print(find(9))
# print(find(6))
# print(find(188))
# print(insert(7))
# print(insert(12))
