def text_reverse(text, N):
    reverse_list = []
    for r in range(N):
        reverse_text = ''
        for c in range(N):
            reverse_text = text[r][c] + reverse_text
        reverse_list.append(reverse_text)
    return reverse_list


def text_col(text, N):
    reverse_list = []
    for c in range(N):
        reverse_text = ''
        for r in range(N):
            reverse_text = reverse_text + text[r][c]
        reverse_list.append(reverse_text)
    return reverse_list


def brute(text, N, M):
    # reverse_text = text_reverse(text, N)
    m = round(M/2)
    for n in range(N):
        for j in range(N-M+1):
            if text[n][j:j+M] == text[n][j+M-1:j+M-m]:
                return text[n]
        # if text[n][:M//2] == text[n][:(M//2)-1:-1]:
        #     return text[n]

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())    # N =  전체 텍스트의  M = 찾을 패턴의 길이
    text = [(input()) for _ in range(N)]

    print(brute(text, N, M))
    # print(f'#{tc} {text_reverse(text, N)}')
    # print('-----------------------------------------')
    # print(f'#{tc} {text_reverse(text_col(text, N), N)}')

# def text_reverse(text, N):
#     reverse_list = []
#     for c in range(N):
#         reverse_text = ''
#         for r in range(N):
#             reverse_text = reverse_text + text[r][c]
#         reverse_list.append(reverse_text)
#     return reverse_list


# TC = int(input())
# for tc in range(1, TC+1):
#     N, M = map(int, input().split())    # N =  전체 텍스트의  M = 찾을 패턴의 길이
#     text = [(input()) for _ in range(N)]
#
#     for n in range(N):
# #         for j in range(N-M+1):
# #             patt = text[n][j:j+M]
# #             if patt in text_reverse(text, N)[n][]: