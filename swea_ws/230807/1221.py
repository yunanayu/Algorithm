# pattern = ['ZRD', 'ONE', 'TWO']
# original = list('ZRD ZRD ONE TWO ZRO'.split())
#
# result = []
# for n in original:
#     for i in range(3):
#         if pattern[i] == n:
#             result.append(i)
#             break
#
# pattern = {'ZRD':0,'ONE': 1, 'TWO': 2 }
# for n in original:
#     result.append(pattern[n])

TC = int(input())
for tc in range(1, TC+1):
    