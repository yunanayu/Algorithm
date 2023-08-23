# 10진수 => 2진수의 문자열 7=>'111'
def decToBin(decV):
    result = ''
    for shiftBit in range(4):
        t = decV & (1<<shiftBit)    # 결과값은 0 or 다른숫자 1개
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result

    return result


print(bin(6))
print(decToBin(6))

# 1100 => 12
# 123 => ((1*10+2)*10)+3
def BinToDec(Bins):
    result = 0
    for c in Bins:
        result = result * 2 + int(c)
        # result = result<<1 | int(c)
    return result


print((BinToDec('1101')))

# '10A' => 266
def HexToDec(HexS):
    result = 0
    for c in HexS:
        if c.isdecimal():
            t = int(c)
        else:
            t = ord(c) - ord('A') + 10
        result = result*16 + t
    return result

print(HexToDec('10A'))

# A => '1010'
def HexToBin(HexC):
    # 16진수 => 10진수
    if HexC.isdecimal():
        decV = int(HexC)
    else:
        decV = ord(HexC) - ord('A') + 10

    # 10진수 => 2진수 문자열
    result = ''
    for shiftBit in range(4):
        t = decV & (1 << shiftBit)  # 결과값은 0 or 다른숫자 1개
        if t != 0:
            result = '1' + result
        else:
            result = '0' + result
    return result

print(HexToBin('A'))

def HexToBin2(HexC):
    pass