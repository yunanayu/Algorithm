# 이진수
import sys
sys.stdin = open('input.txt','r')

def HexToBin(HexC):

    # 16진수 -> 2진수
    if HexC.isdecimal():
        decV = int(HexC)
    else:
        decV = ord(HexC) - ord('A') + 10

    result = ''

    for shiftBit in range(4):
        t = decV & (1 << shiftBit)
        if t!=0:
            result = '1' + result
        else:
            result = '0' + result
    return result


TC = int(input())
for tc in range(1, TC+1):
    a, S = list(input().split())
    N = int(a)
    print(f'#{tc}', end=' ')
    for s in S:
        print(HexToBin(s), end='')
    print()
