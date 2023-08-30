def partial(k, sumV, result):
    if k == N:
        print(bits)
        #
        print(sumV, result)
        return

    bits[k] = 0
    partial(k+1, sumV, result)
    bits[k] = 1
    # sumV += numbers[k]          # => 사용하지 않기
    # result.append(numbers[k])   # => 사용하지 않기
    partial(k+1, sumV+numbers[k], result + [numbers[k]])    # result.append 사용하게 되면 계속 호출 됨


N = 4
numbers = [8, 10, 20, 3]
bits = [-1] * N
result = []
partial(0,0,result)