# 반복문자 지우기

# TC = int(input())
# for tc in range(1, TC+1):
#     txt = list(input())
#     N = len(txt)
#     i = 0
#     while i+1 < len(txt):
#         # for i in range(N-1):
#         if txt[i] == txt[i+1]:
#             txt.pop(i+1)
#             txt.pop(i)
#             i = 0
#         else:
#             i += 1
#     # print(txt)
#     # # txt.pop()
#     # print(txt)
#     print(f'#{tc} {len(txt)}')

# TC = int(input())
# for tc in range(1, TC+1):
#     txt = list(input())
#     N = len(txt)

#---------------------------------------------
# TC = int(input())
# for tc in range(1, TC+1):
#     txt = list(input())
#     N = len(txt)
#     i = 0
#     while i+1 < len(txt):
#         if txt[i] == txt[i+1]:
#             txt.pop(i+1)
#             txt.pop(i)
#             i = 0
#         else:
#             i += 1
#
#     print(f'#{tc} {len(txt)}')
#--------------------------------------------------

TC = int(input())
for tc in range(1, TC+1):
    txt = input()
    ST = []
    for t in txt:
        if not ST or ST[-1] != t:
            ST.append(t)
        else:
            ST.pop()
    print(f'#{tc} {len(ST)}')
