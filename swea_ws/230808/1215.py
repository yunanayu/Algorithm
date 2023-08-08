# [S/W 문제 해결 기본] 3일차 - 회문1
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
    arr = [(input()) for _ in range(8)]
    cnt = 0
    arr2 = arr_col(arr, 8)   # 열 우선
    for i in range(8):
        for j in range(8-L+1):
            if arr[i][j:j+L] == arr[i][j:j+L][::-1]:
                cnt += 1
    for i in range(8):
        for j in range(8-L+1):
            if arr2[i][j:j+L] == arr2[i][j:j+L][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')