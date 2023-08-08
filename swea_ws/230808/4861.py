# 회문

def text_col(text, N):
    col_list = []
    for c in range(N):
        col_text = ''
        for r in range(N):
            col_text = col_text + text[r][c]
        col_list.append(col_text)
    return col_list

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())    # N =  전체 텍스트의  M = 찾을 패턴의 길이
    text = [(input()) for _ in range(N)]
    text2 = text_col(text, N)

    for i in range(N):
        for j in range(N-M+1):
            if text[i][j:j+M] == text[i][j:j+M][::-1]:
                print(f'#{tc}', text[i][j:j+M])

    for i in range(N):
        for j in range(N-M+1):
            if text2[i][j:j + M] == text2[i][j:j + M][::-1]:
                print(f'#{tc}', text2[i][j:j + M])