def subset(k):
    if k==N:
        print(result)
        sumV = 0 # 합
        for i in range(N):
            if result[i]:
                sumV += lst[i]   # 합
                print(lst[i], end=' ')
        print('=>', sumV)
        return

    result[k] = 0
    subset(k+1)
    result[k] = 1
    subset(k+1)


'''
[0, 0, 0]
=> 0
[0, 0, 1]
10 => 10
[0, 1, 0]
3 => 3
[0, 1, 1]
3 10 => 13
[1, 0, 0]
2 => 2
[1, 0, 1]
2 10 => 12
[1, 1, 0]
2 3 => 5
[1, 1, 1]
2 3 10 => 15
'''

# def subset(k):
#     if k == N:
#         print(result)
#         return
#
#     for i in [0,1]:
#         result[k] = i
#         subset(k+1)
#
#
#
# '''
# [0, 0, 0]
#
# [0, 0, 1]
# 10
# [0, 1, 0]
# 3
# [0, 1, 1]
# 3 10
# [1, 0, 0]
# 2
# [1, 0, 1]
# 2 10
# [1, 1, 0]
# 2 3
# [1, 1, 1]
# 2 3 10
# '''



lst = [2, 3, 10]
N = len(lst)
result = [-1] * N
subset(0)


