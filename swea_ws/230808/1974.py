# 스도쿠 검증


# def search(data_list):
#     for i in data_list:
#         if i != 1:
#             return 0
#         else:
#             break
#     return 1
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     arr_search = [[0] * 10 for _ in range(27)]
#     arr_search[0][0] = 1
#     for r in range(9):
#         for c in range(9):
#             arr_search[arr[r][c]] += 1
#     print(arr_search)

def search(data):
    arr_search = [0] * 10
    arr_search[0] = 1
    for n in data:
        arr_search[n] += 1
    for i in arr_search:
        if i != 1:
            return False
        else:
            break
    return True

TC = int(input())

for tc in range(1, TC+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    for r in range(9):
        new_arr1 = []
        for c in range(9):
            new_arr1.append(arr[r][c])
        if search(new_arr1):
            continue
        else:

    # for r in range(9):
    #     new_arr2 = []
    #     for c in range(9):
    #         new_arr2.append(arr[c][r])
    # for r in range(0, 7, 3):
    #     new_arr3 = []
    #     for c in range(0, 7, 3):
    #         for i in range(3):
    #             new_arr3.append(arr[r + i][c + i])
    # if search(new_arr1) and search(new_arr2): # and search((new_arr3)):
    #     print(f'#{tc}', 1)
    # else:
    #     print(f'#{tc}', 0)
    #



