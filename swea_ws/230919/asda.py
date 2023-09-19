N, M = map(int, input().split())
lst = []    # M개의 수열을 저장하기 위한 리스트

def dfs():
    if len(lst) == M:   # M의 갯수 만큼 뽑아 냈다면
        print(*lst)
        return

    for i in range(1, N+1): # 1부터
        if i not in lst:    # 중복 허용 유무
            lst.append(i)
            dfs()
            lst.pop()
            # lst : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4] -> [1] 1싸이클
            # 출력   pop() 순서로 반복

dfs()   # 모든 가능한 수열을 생성