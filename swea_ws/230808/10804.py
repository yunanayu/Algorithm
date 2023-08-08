def text_reverse(text, N):
    # reverse_list = []
    reverse_text = ''
    for r in range(N):
        reverse_text = text[r] + reverse_text
        # reverse_list.append(reverse_text)
    return list(reverse_text)


TC = int(input())
for tc in range(1, TC+1):
    txt = list(input())
    txt2 = text_reverse(txt, len(txt))
    txt3 = {'b':'d', 'd':'b', 'q':'p', 'p':'q'}
    for i in txt2:
        if txt2[i] == 'b':
            txt2[i] = 'd'

    print(f'#{tc}', ''.join(txt2))
# #
# txt3 = {'b':'d'}
# print(txt3['b'])




