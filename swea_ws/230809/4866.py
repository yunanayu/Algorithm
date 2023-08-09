# 괄호검사
TC = int(input())
for tc in range(1, TC+1):
    txt = input()
    ST = []
    result = 1
    for t in txt:
        if t in ['{', '(']:
            ST.append(t)

        elif t in ['}', ')']:
            if ST:                      # 데이터가 있을때만 pop 가능
                checkT = ST.pop()
                if checkT == '{' and t == ')':
                    result = 0
                elif checkT == '(' and t == '}':
                    result = 0
            else:
                result = 0
                break
    if ST:
        result = 0
    print(f'#{tc} {result}')
#--------------------------------------------
# line 11-20
# elif c in [')', '}']
#     if ST:
#         checkC = ST.pop()
#         if checkC == '{' and c == ')':
#             result = 0
#         elif checkC == '(' and c == '}':
#             result = 0
#     else:
#         result = 0
#         break