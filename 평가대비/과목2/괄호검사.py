TC = int(input())
for tc in range(1, TC+1):
    code = input()
    ST = []
    for t in code:
        if t in ['{', '(']:
            ST.append(t)
        elif t in ['}', ')']:
            if ST:
                if ST[-1] == '{' and t == '}':
                    ST.pop()
                elif ST[-1] == '(' and t == ')':
                    ST.pop()
    if ST:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 1)