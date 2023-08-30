def perm(k):
    if k == N:
        # print(bits)
        for i in range(N):
            pos = bits[i]
            print(numbers[pos], end=' ')
        print()
        return

    for i in range(N):      # 사용여부 따지기
        if not used[i]:
            bits[k] = i     # k 번째 값에 답을 덮어쓰고 있기 때문에 원복 필요 없음
            used[i] = True
            perm(k+1)
            used[i] = False     # 다음 반복을 위해 원상복구

N = 4
numbers = [8, 10, 20, 3]
used = [False]*N
bits = [-1] * N
# perm(1) # -> 0번은 고정시키고 진행
#or
# bits[0] = 0
# used[0] = True
# perm(1)
'''
3 8 10 20 
3 8 10 3 
3 8 20 10 
3 8 20 3 
3 8 3 10 
3 8 3 20 
3 10 8 20 
3 10 8 3 
3 10 20 8 
3 10 20 3 
3 10 3 8 
3 10 3 20 
3 20 8 10 
3 20 8 3 
3 20 10 8 
3 20 10 3 
3 20 3 8 
3 20 3 10 
3 3 8 10 
3 3 8 20 
3 3 10 8 
3 3 10 20 
3 3 20 8 
3 3 20 10 
'''
perm(0)