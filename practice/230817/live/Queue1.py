def enQ(data):
    global rear
    if rear == Qsize - 1:  # 가득 차면 # 실제로 사용할때는 line 3-5 없이 함수 사용하기
        print('Q is full')
    else:
        rear += 1
        Q[rear] = data

def deQ():
    global front
    if front == rear:
        print('Q is empty')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * 3
rear = -1
front = -1

while front != rear:    # 큐가 비어있지 않으면
    front += 1
    print(Q[front])

print(deQ())
print(deQ())
front += 1
tmp = Q[front]
print(tmp)