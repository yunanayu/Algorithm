def partial(k):
    if k == N:
        print(bits)
        sumV = 0
        for i in range(N):
            if bits[i] == 1:
                print(numbers[i], end=' ')
                sumV += numbers[i]
        print()
        print(sumV)
        return

    bits[k] = 0
    partial(k+1)
    bits[k] = 1
    partial(k+1)


N = 4
numbers = [8, 10, 20, 3]
bits = [-1] * N

partial(0)