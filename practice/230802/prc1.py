# 행 우선 순회

N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j])
"""
0
1
2
3
4
5
6
7
"""
# 열 우선 순회

N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for j in range(M):
    for i in range(N):
        print(arr[i][j])  # 혹은 for i , for j , arr[j][i]
'''
0
4
1
5
2
6
3
7
'''
# 지그재그 순회

N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i % 2)])
'''
0
1
2
3
7
6
5
4
'''

N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1,], [4, 5, 6, 7]]
for i in range(N):
    for j in range(len(arr[i])):
        print(arr[i][j])
'''
0
1
4
5
6
7
'''


N = 2
M = 4
arr = [[0] * M for _ in range(N)] #이차원 배열 리스트 생성 방법
arr2 = [[0] * M ] * N # 사용 금지
# arr[0][0] = 1 실행 시 arr은 1행 1열만  1로 바뀌지만  arr2는 1행 1열과 2행 1열 모두 1로 바뀐다.

# ---------------------------------------------------------------------------------------------

# 최댓값 구하기
N = 2 # 행의 크기
M = 4 # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr[i][j]
        if max_v < row_total:
            max_v = row_total