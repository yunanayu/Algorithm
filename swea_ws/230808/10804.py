# 문자열의 거울상


TC = int(input())
for tc in range(1, TC+1):
    txt = list(input())
    txt_mirror = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'}
    new_text = ''
    for i in range(len(txt)):
        new_text = txt_mirror[txt[i]] + new_text
    print(f'#{tc} {new_text}')
