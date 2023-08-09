# full 이면 True
# 아니면 False
def isFull():
    if top == Size - 1:
        return True
    else:
        return False


# 입력이 불가능한 경우 -1 을 return
# 입력에 문제가 없는 경우 return top
def push(item):     # 몇개를 쌓을지 정하고 시작
    global top      # top 은 전역변수임
    # if isFull():
    if top == Size - 1:
        print('overflow')
        return -1
    top += 1
    ST[top] = item
    return top


# 스택이 비어있으면 -1
# 아니면 top 위치에 있는 item return
def pop():
    global top
    if top == -1:   # 비어있는지 확인 방법 1
    # if isEmpty(): # 비어있는지 확인 방법 2
        print('underflow')
        return -1
    result = ST[top]    # 방법 1
    top -= 1
    return result     # <- 더 좋은 방법임
    # top -= 1          # 방법 2
    # return ST[top+1]


def peak():     # 가장 윗 값을 가져올 때 / 비어있는지 꼭 확인
    if top == -1:  # 비어있는지 확인 방법 1
    # if isEmpty(): # 비어있는지 확인 방법 2
        return ST[top]

Size = 10
ST = [-1] * Size  # 0 이상의 데이터만 들어올것임.
top = -1        # top -> 가장 마지막에 들어간 데이터. 아무것도 없을땐  top = -1
lst = [4, 5, 6, 10]
for d in lst:
    push(d)
print(ST)
print(pop(), top)   # top 을 기준으로 데이터를 넣었다 뺐다 하고 있기 때문에 데이터를 바꿀 순 없다.

#-----------------------------------------------------------------------------------------
# 파이썬 함수 사용

ST_P = []
for d in lst:
    ST_P.append(d)      # 데이터가 없을 때 pop 을 하면 오류
if len(ST_P) > 0:       # pop 하기전에 데이터가 1개 이상인지 꼭 체크 (size 확인)
# if ST_P:  # 리스트에 데이터 있는지 확인하는 방법 2
    print(ST_P.pop())

# push -> append
# pop => pop  꼭 길이체크 해주기