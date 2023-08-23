# 이진수
import sys
sys.stdin = open('input.txt','r')

def HexToBin(HexC):
    ans = ''
    # 16진수 -> 2진수
    for c in HexC:
        if c.isdecimal():
            decV = int(c)
        else:
            decV = ord(c) - ord('A') + 10
        result = ''
        for shiftBit in range(4):
            t = decV & (1 << shiftBit)
            if t!=0:
                result = '1' + result
            else:
                result = '0' + result
        ans = ans + result
    return ans


TC = int(input())
for tc in range(1, TC+1):
    a, S = list(input().split())
    N = int(a)
    print(f'#{tc} {HexToBin(S)}')
