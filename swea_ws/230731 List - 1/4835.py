T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    sum_list = []
    for i in range(n-2):
        sum = 0
        for _ in range(m):
            sum = sum + int(numbers[i])
            i += 1
        sum_list.append(sum)
    cur_min = 100000000
    cur_max = -1
    for s in sum_list:
        if cur_min > i:
            cur_min = i
        elif cur_max < i:
            cur_max = i
    print(f'#{test_case} {cur_max - cur_min}')