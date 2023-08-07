# # 문자열
#
# str1 =
# str2 =
# # print(str2.count('Y'))
#
# for str1 의 각각 문자 k에 대하여ㅣ
#     c = str2.count(k)
#     if maxV < c:
#         maxV = c
#
TC = int(input())
for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    ans = 0
    if str1 in str2:
        ans += 1
    else:
        ans = 0
    print(f'#{tc} {ans}')

