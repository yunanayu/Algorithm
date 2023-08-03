nums = [64, 25, 10, 22, 11]
N = 5
'''
N-1 : [11, 24, 10, 22, 64]
N-2 : [11, 22, 10, 25, 64]
N-3 : [11, 10, 22, 25, 64]
N-4(1) : [10, 11, 22, 25, 64]
'''
# for e in range(N-1, 0, -1):
#     curMaxIdx = 0
#     for idx in range(1, e+1):
#         if nums[curMaxIdx] < nums[idx]:
#             curMaxIdx = idx
#
#     nums[curMaxIdx], nums[e] = nums[e], nums[curMaxIdx]
# print(nums)

# 버블 정렬
# nums = [64, 25, 10, 22, 11]
# N-1 : [25, 64 ..], [25, 10, 64, ...], [25, 10, 22, 64, 11]...

for phase in range(N-1, 0, -1):
    for idx in range(phase):
        if nums[idx] < nums[idx+1]:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]








# for s in range(N-1):
#     # 최소를 구한다. s -> N-1
#     for idx in range(s+1, N):
#         curMin_idx = s
#         if nums[curMin_idx] > nums[idx]:
#             curMin_idx = idx
#         nums[curMin_idx], nums[s] = nums[s], nums[curMin_idx]
# print(nums)