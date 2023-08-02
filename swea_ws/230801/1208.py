#
# def cur_min(data_list):
#     cur_min = 10000
#     min_idx = 0
#     for idx in range(len(data_list)):
#         value = data_list[idx]
#         if cur_min > value:
#             min_idx = idx
#     return min_idx
#
# def cur_max(data_list):
#     cur_max = 0
#     max_idx = 0
#     for idx in range(len(data_list)):
#         value = data_list[idx]
#         if cur_max < value:
#             max_idx = idx
#     return max_idx
#
# TC = 10
#
# for tc in range(1, TC+1):
#     d_nums = int(input())
#     box = list(map(int, input().split()))
#     for n in range(d_nums):
#         b = cur_min(box)
#         d = cur_max(box)
#         box[b] += 1
#         box[d] -= 1
#     print(f'#{tc} {max(box)-min(box)}')


TC = 10

for tc in range(1, TC+1):
    d_nums = int(input())
    box = list(map(int, input().split()))
    for n in range(d_nums):
        box_max = max(box)
        box_min = min(box)
        max_idx = box.index(box_max)
        min_idx = box.index(box_min)
        box[min_idx] += 1
        box[max_idx] -= 1
    print(f'#{tc} {max(box)-min(box)}')

