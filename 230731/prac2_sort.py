nums = [55, 7, 78, 12, 42]
N = len(nums)

for i in range(0, N-1):
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)

#N-1(4)
    def bubble_sort(nums):
        N = len(nums)
        for j in range(N-1, 0, -1):
            for k in range(0, j):
                if nums[k] > nums[k+1]:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
        return

    def bubble_sort2(nums):
        N = len(nums)
        for i in range(N-1, 0, -1):
            for j in range(i):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return

nums = [55 , 7, 21, 56, 72 , 12]
bubble_sort(nums)
print(nums)

bubble_sort2(nums)
print(nums)