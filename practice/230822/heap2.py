def insert(item):
    global last

    last += 1
    Heap[last] = item
    c = last
    while c > 1:
        p = c//2
        if Heap[p] < Heap[c]:
            Heap[p], Heap[c] = Heap[c], Heap[p]
            c = p
        else:
            break


def insert1(item):
    global last

    last += 1
    Heap[last] = item
    c = last
    p = c // 2
    while c > 1 and :
        if Heap[p] < Heap[c]:
            Heap[p], Heap[c] = Heap[c], Heap[p]
            c = p


def pop():
    global last
    result = Heap(1)
    Heap[1] = Heap[last]
    last -= 1

    p = 1
    c = p*2

    while c <= last:
        if c+1 <= last and Heap[c] < Heap[c+1]  :  # dfssssrdjqd
            c = c+1
        if Heap[p] < Heap(c):
            Heap[p], Heap[c] = Heap[c], Heap[p]
            p = c
            c = p*2
        else:
            break
    return result

Heap = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19] + [0] * 100
last = 9

# insert(32)
# print(Heap)
# [0, 33, 32, 27, 21, 31, 18, 23, 14, 19, 22, 0, 0]

# insert(20)
# print(Heap)