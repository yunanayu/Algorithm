nums = [1, 2, 3]
n = 3
for i0 in range(n):
    for i1 in range(n):
        if i0 != i1:
            for i2 in range(n):
                if i2 != i0 and i2 != i1:
                    print(i0, i1, i2)
                    print('---------------------------')
                    print(nums[i0], nums[i1], nums[i2])


num = input()
num_lst = list(map(int,num))
print(num_lst)

int_num = int(num)
num_lst1 = []
while int_num > 0:
    num_lst1.append(int_num % 10)
    int_num = int_num // 10
print(num_lst1)