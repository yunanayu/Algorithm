TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(0, N-1):
        max_idx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if nums[max_idx] < nums[j]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]
        min_idx = i
        if i % 2 != 0:
            for j in range(i+1, N):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            # if j+1 < N and nums[j+1] == 1:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    print(f'#{tc}' , *nums[:10])




# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     for i in range(0, N, 2):
#         max_idx = i
#         for j in range(i+1, N):
#             if nums[max_idx] < nums[j]:
#                 max_idx = j
#         nums[j], nums[max_idx] = nums[max_idx], nums[j]
#         min_idx = i+1
#         for k in range(i+2, N):
#             if nums[min_idx] > nums[k]:
#                 min_idx = j
#         nums[j+1], nums[min_idx] = nums[min_idx], nums[j+1]
            # if j+1 < N and nums[j+1] == 1:
                
                
    # print(nums)



#  for i in range(0, N-1, 2):
#         max_idx = i
#         min_idx = i+1
#         for j in range(i+1, N):
#             if nums[max_idx] < nums[j]:
#                 max_idx = j
#             elif nums[min_idx] > nums[j]:
#                 min_idx = j
#             if j+1 < N and nums[j+1] == 1:
#                 nums[j], nums[max_idx] = nums[max_idx], nums[j]
#                 nums[j+1], nums[min_idx] = nums[min_idx], nums[j+1]
#     print(nums)



    #     max_idx = i
    #     min_idx = i
    #     for j in range(i + 1, N // 2):
    #         if nums[max_idx] < nums[j]:
    #             max_idx = 2 * j
    #             nums[max_idx], nums[j] = nums[j], nums[max_idx]
    #         elif nums[min_idx] > nums[j]:
    #             min_idx = 2 * j - 1
    #             nums[min_idx], nums[j] = nums[j], nums[min_idx]
    # print(nums)