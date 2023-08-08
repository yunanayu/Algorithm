# def text_reverse(text, N):
#     # reverse_list = []
#     reverse_text = ''
#     for r in range(N):
#         reverse_text = text[r] + reverse_text
#         # reverse_list.append(reverse_text)
#     return list(reverse_text)


TC = int(input())
for tc in range(1, TC+1):
    txt = list(input())
    txt_mirror = {'b': 'd', 'd': 'b', 'q': 'p', 'p': 'q'}
    new_text = ''
    for i in range(len(txt)):
        new_text = txt_mirror[txt[i]] + new_text
    print(f'#{tc} {new_text}')
# #
# # txt3 = {'b':'d'}
# # print(txt3['b'])

# txt3 = {'b':'d', 'd':'b', 'q':'p', 'p':'q'}
# print(str(txt3['b']))
#
#

TC = int(input())
for tc in range(1, TC+1):
    txt = list(input())
    # print(text_reverse(txt, len(txt)))
    txt2 = text_reverse(txt, len(txt))
    txt3 = {'b':'d', 'd':'b', 'q':'p', 'p':'q'}
    for i in txt2:
        txt2[i] = txt3[txt2[i]]+ new_text
    print(f'#{tc}', ''.join(txt2))#