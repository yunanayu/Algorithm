# 초심자의 회문 검사

T = int(input())
for t in range(1, T+1):
    text = input()
    text_reverse = ''
    for txt in text:
        text_reverse = txt + text_reverse
    if text == text_reverse:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')