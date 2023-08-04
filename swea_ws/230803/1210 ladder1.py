TC = 1
for i in range(1, TC+1):
    arr = [list(map(int, input().split()))*100 for _ in range(100)]
    print(len(arr[0]))
print()




# T = 10
#
# for _ in range(T):
#     tc = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     #print(arr)
#
#     for c in range(100):
#         if arr[99][c] == 2:
#             break
#
#     # print(c)
#
#     for r in range(98, 0, -1):
#         if c-1 >= 0 and arr[r][c-1] == 1: # 왼쪽에 1이 있으면
#             while c-1 >= 0 and arr[r][c-1] == 1: # 왼쪽에 1인 동안 왼쪽으로 좌표 이동
#                 c -= 1
#
#         elif c+1 < 100 and arr[r][c+1] == 1: # 오른쪽에 1이 있으면
#             while c+1 < 100 and arr[r][c+1] == 1: # 오른쪽이 1인 동안 오른쪽으로 좌표 이동
#                  c += 1