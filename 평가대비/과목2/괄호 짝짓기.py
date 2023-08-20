# for tc in range(1, 11):
#     N = int(input())
#     case = input()
#     ST = []
#     result = 1
#     for i in case:
#         if i in ['{', '[', '(', '<']:
#             ST.append(i)
#         elif i in ['}', ']', ')', '>']:
#             if ST:
#                 if ST[-1] == '{' and i == '}':
#                     ST.pop()
#                     continue
#                 elif ST[-1] == '[' and i == ']':
#                     ST.pop()
#                     continue
#                 elif ST[-1] == '(' and i == ')':
#                     ST.pop()
#                     continue
#                 elif ST[-1] == '<' and i == '>':
#                     ST.pop()
#
#
#     if ST:
#         result = 0
#     print(f'#{tc} {result}')
#

for tc in range(1, 11):
    N = int(input())
    case = input()
    ST = []
    result = 1
    for i in case:
        if i in ['{', '[', '(', '<']:
            ST.append(i)
        elif i in ['}', ']', ')', '>']:
            if ST:
                check = ST.pop()
                if check == '(' and i != ')':
                    result = 0
                elif check == '{' and i != '}':
                    result = 0
                elif check == '[' and i != ']':
                    result = 0
                elif check == '<' and i != '>':
                    result = 0
    print(f'#{tc} {result}')