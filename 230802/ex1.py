# 절댓값 함수
def my_abs(value):
    if value < 0:
        return -value
    return value
    # = return value if value > 0 else -value


#2차원 배열
# N = 5
# nums = [[0] * 5 for _ in range(N)]
# nums[2][2] =1
# print(nums)
#------------------------------------------
#1씩 더하기
#
# value = 1
# for r in range(N):
#     for c in range(N):
#         nums[r][c] = value
#         value += 1
# print(nums)
#-----------------------------------------------
# 행우선으로 좌표 출력하기

N = 5
nums = [[0] * 5 for _ in range(N)]

d = 0
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 방향 순서 상관없는 경우
# r= 001-1, c= 1-100 으로 만들고 풀면 됨

#좌표값 구하기
for r in range(N):
    for c in range(N):
        print('------------------')
        print(r,c, nums[r][c])
        for d in range(4):
            newR = r+dr[d]
            newC = c+dc[d]
            if 0<= newR < N and 0<= newC < N:
                print(newR, newC, nums[newR][newC])
        # print(r+0,c-1) #왼쪽
        # print(r-1,c+0) #위쪽
        # print(r+0,c+1) #오
        # print(r+1, c+0) #아래