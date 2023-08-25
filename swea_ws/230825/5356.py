# 의석이의 세로로 말해요

import sys
sys.stdin = open('input_5356.txt', 'r')

# TC = int(input())
# for tc in range(1, TC+1):
#     arr = [list(input()) for _ in range(5)]
#     max_len = 0
#     for r in range(5):
#         cur_len = len(arr[r])
#         if max_len < cur_len:
#             max_len = cur_len
#     for r in range(5):
#         arr[r] = arr[r] + ['.']*(15-len(arr[r]))
#     # print(arr)
#     result = ''
#     for c in range(max_len):
#         for r in range(5):
#             if arr[r][c] != '.':
#                 result = result + arr[r][c]
#     print(result)

TC = int(input())
for tc in range(1, TC + 1):
    arr = [list(input()) for _ in range(5)]
    for r in range(5):
        arr[r] = arr[r] + ['.'] * (15 - len(arr[r]))
    result = ''
    for c in range(15):
        for r in range(5):
            if arr[r][c] != '.':
                result = result + arr[r][c]
    print(f'#{tc} {result}')


    # max_len = 0
    # for r in range(5):
    #     cur_len = len(arr[r])
    #     if max_len < cur_len:
    #         max_len = cur_len
    # result = ''
    # for r in range(5):
    #     for c in range(max_len):
    #         # if len(arr[r]) > max_len:
