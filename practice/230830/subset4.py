def partial(k, sumV, zerolist, onelist):
    if k == N:
        print(bits)
        print(sumV, onelist)
        return

    bits[k] = 0
    partial(k+1, sumV, zerolist+[numbers[k]], onelist)
    bits[k] = 1
    # sumV += numbers[k]          # => 사용하지 않기
    # result.append(numbers[k])   # => 사용하지 않기
    partial(k+1, sumV+numbers[k], zerolist, onelist+[numbers[k]])    # result.append 사용하게 되면 계속 호출 됨


N = 4
numbers = [8, 10, 20, 3]
bits = [-1] * N
zerolist = []       # 재귀함수이므로 함수 바깥에서 리스트 선언해주기
onelist = []
partial(0,0,zerolist,onelist)
#or
# partial(0,0,[],[])