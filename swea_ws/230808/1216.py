# [S/W 문제해결 기본] 3일차 - 회문2



# # str_value 이 palidrom 이면 1을
# # 아니면 0을 return 하는 함수
# def isPalidrom(str_value, M):
#     ..
#     result = 1
#     return
# origin_str = 'CBCABBAC'
# M = 4
# for s in range():
#     new_str =
#     cnt += isPalidrom(new_str, M)

def arr_col(arr, length):
    col_list = []
    for r in range(length):
        col_arr = ''
        for c in range(length):
            col_arr = col_arr + arr[c][r]
        col_list.append(col_arr)
    return col_list


for tc in range(1, 11):
    L = int(input())
    arr = [(input()) for _ in range(100)]
    arr2 = arr_col(arr, 100) # 열 우선
    max_len = 0
    for l in range(1, 101):
        for i in range(100):
            for j in range(100-l+1):
                if arr[i][j:j+l] == arr[i][j:j+l][::-1]:
                    if max_len < len(arr[i][j:j+l]):
                        max_len = len(arr[i][j:j+l])
    for l in range(1, 101):
        for i in range(100):
            for j in range(100-l+1):
                if arr2[i][j:j+l] == arr2[i][j:j+l][::-1]:
                    if max_len < len(arr[i][j:j + l]):
                        max_len = len(arr[i][j:j + l])
    print(f'#{tc} {max_len}')