def bubble_sort():
    pass

# 55 21 11 67 100 12

T = 1
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    N = len(nums)
    for phase in range(N-1, 0, -1):
        # N 이 6이라면  phase : 5
        #0-1,1-2,2-3,3-4,4-5 : 0-4
        #phase : 4
        #0-1, 1-2, 2-3, 3-4 : 0-3
        for j in range(0, phase):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums)

#reverse sort

T = 1
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    N = len(nums)
    for phase in range(N-1):
        # N 이 6이라면
        # phase : 0 : N-1, N-2, ,,, 1-0 N-1 ~ 1
        # phase : 1 : N-1, N-2, ,,, 2-1 N-1 ~ 2
        for j in range(N-1, phase , -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]

    print(nums)