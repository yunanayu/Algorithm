# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     nums = list(map(int, input()))
#     num_cnt = [0] * 10
#     for i in range(N):
#         num_cnt[nums[i]] +=1
#         m = max(num_cnt)
#         n = num_cnt.index(m)
#     print(num_cnt)
#     print(f'#{tc} {n} {m}')
#
def num_max(data):
    cur_max = -1
    for i in data:
        if cur_max < i:
            cur_max = i
    return cur_max

def num_idx(data_list):
    curM = 0
    curMI = 0
    for idx in range(len(data_list)):
        value = data_list[idx]
        if curM <= value:
            curM = value
            curMI = idx
    return curMI


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input()))
    num_cnt = [0] * 10
    for i in nums:
        num_cnt[i] += 1
        m = num_max(num_cnt)
        n = num_idx(num_cnt)

    print(f'#{tc} {n} {m}')
