def enque(item):
    global hsize

    hsize += 1
    Tree[hsize] = item

    child = hsize
    parent = child // 2

    while parent and Tree[parent] < Tree[child]: # parent 가 더 크면 종료 # parent 가 0이 아니여야함
        Tree[parent], Tree[child] = Tree[child], Tree[parent]
        child = parent
        parent = child//2


def deque():
    global hsize
    result = Tree[1]
    Tree[1] = Tree[hsize]
    hsize -= 1

    parent = 1
    child = parent*2

    while child <= hsize:
        if child+1 <= hsize and Tree[child] < Tree[child+1]:
            child = child + 1
        if Tree[parent] < Tree[child]:
            Tree[parent], Tree[child] = Tree[child], Tree[parent]

            parent = child
            child = parent * 2

        else:
            break

    return result

Tree = [0, 20, 15, 19, 4, 13, 11]
Tree += [0]*100
hsize = 6
enque(23)
print(Tree)
enque(17)
print(Tree)

result = deque()
print(result)
print(Tree)