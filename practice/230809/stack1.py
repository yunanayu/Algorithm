stack = [0] * 10
top = -1

top += 1            # push(1)
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3

print(stack[top])
top -= 1
top -= 1
print(stack[top+1])     # 저장은 1,2,3 이지만 꺼내는건 3, 2 순서이다.