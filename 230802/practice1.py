nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
        ]
N = len(nums) # 행의 개수
M = len(nums[0])

# print(len(nums))


for i in range(len(nums)):
    # print(i, nums[i])

for n in nums:
    print(n)

# 행 우선

for r in range(len(nums)):
    for c in range(len(nums[r])):
        print(nums[r][c], end=' ')
    print()
# 열 우선
c = 0
for c in range(M):
    for r in range(N):
        print(nums[r][c], end=' ')
    print()
print('========================')
# 합 구하기

for i in range(len(nums)):
    sum_v = 0
    for c in range(M):
        print(nums[r][c])
        sum_v += nums[r][c]
    print

for n in nums:
    sum_v = 0
    for item in n:
        sum_v += item
    print(n)
# --------------------------------------------------
cur_max = 0

for i in range(len(nums)):
    sum_v = 0
    for c in range(M):
        print(nums[r][c])
        sum_v += nums[r][c]
    print
        if cur_max < sum_v
            cur_max = sum_v

#---------------------------------------------
# 대각선 합
sumV = 0
for i in range(M):
    sumV += nums[i][i]
print((sumV))
#-------------------------
# 반대 대각선 합
for i in range(M):
    sumV += nums[i][M-1-i]
print(sumV)

sumV1 = 0
sumV2 = 0
for i in range(M):
    sumV1 += nums[i][i]
    sumV2 += nums[i][M-1-i]
print(sumV1, sumV2)
