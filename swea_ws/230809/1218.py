# [S/W 문제 해결 기본] 4일차 - 괄호 짝짓기

for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    ST = []
    dct = {'(':')', ')':'(', '[':']', ']':'[', '{':'}', '}':'{', '<':'>', '>':'<'}
    for a in arr:
        if not ST or dct[ST[-1]] !=
            ST.append(a)
        else:
            ST.pop()
