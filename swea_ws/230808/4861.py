# 회문

# def brute(text, N, M):
#     for n in range(N):
#         if text[n][:M//2] == text[n][:(M//2)-1:-1]:
#             return text[n]
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())    # N =  전체 텍스트의  M = 찾을 패턴의 길이
#     text =[(input()) for _ in range(N)]
#     print(brute(text, N, M))
#---------------------------------------------------------------------------------
N = 20
M = 13
M_1 = round(M/2)
text = [(input()) for _ in range(20)]

# for n in range(N):
#     if text[n][:M//2] == text[n][:(M//2)-1:-1]:
#         print(text[n])

reverse_list = []
for c in range(N):
    reverse_text = ''
    for r in range(N):
        reverse_text = reverse_text + text[r][c]
    reverse_list.append(reverse_text)
print(reverse_list)
print(reverse_list[0][:M_1])
print(reverse_list[0][M//2:M])

 # for i in range(N):
 #    for j in range(N-M+1):
 #        if reverse_list[i][j:j+(M//2)] == reverse_list[i][j:j+(M//2-1):-1]:
 #            return reverse_list[i]
 #        if text[i][:M//2] == text[i][:(M//2)-1:-1]:
 #            return text[i]

# == reverse_list[n][:(M//2)-1:-1]
#-------------------------------------------------------------------------------------
    # for n in range(N):
    #     if reverse_text[n][:5]:
    #         print(reverse_text[n])
#-----------------------------------------------------------------------------------------
# N = 10
# M = 10
# text = [(input()) for _ in range(10)]
#
#
# for c in range(N):
#     reverse_text = ''
#     for r in range(N):
#         reverse_text = reverse_text + text[r][c]
#     print(reverse_text)

# print(text[0][0:M//2])
# print(text[0][:(M//2)-1:-1])
# print(len(text))

#------------------------------------------------------------------------------------
# def brute(text, N, M):
#
#     reverse_list = []
#     for c in range(N):
#         reverse_text = ''
#         for r in range(N):
#             reverse_text = reverse_text + text[r][c]
#         reverse_list.append(reverse_text)
#
#
#     # for n in range(N):
#     #     if reverse_list[n][:M//2] == reverse_list[n][:(M//2)-1:-1]:
#     #         return reverse_list[n]
#     #     if text[n][:M//2] == text[n][:(M//2)-1:-1]:
#     #         return text[n]
#
#
#     for i in range(N):
#         for j in range(N-M+1):
#             if reverse_list[i][j:j+(M//2)] == reverse_list[i][j:j+(M//2-1):-1]:
#                 return reverse_list[i]
#             if text[i][:M//2] == text[i][:(M//2)-1:-1]:
#                 return text[i]
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())    # N =  전체 텍스트의  M = 찾을 패턴의 길이
#     text = [(input()) for _ in range(N)]
#     print(f'#{tc} {brute(text, N, M)}')
