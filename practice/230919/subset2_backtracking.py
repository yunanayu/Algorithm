def subset(k, cur_sum):
    if cur_sum > 10:
        return

    if k==N:
        print(result)
        if cur_sum == 10:
            for i in range(N):
                if result[i]:
                    print(lst[i], end=' ')
            print()
        return


    result[k] = 0
    subset(k+1, cur_sum)
    result[k] = 1
    subset(k+1, cur_sum+lst[k])


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 3
result = [-1] * N
subset(0, 0)


