def BinToDec(Bins):
    result =0
    for c in Bins:
        result = result * 2 + int(c)
    return result
S = '000000011110000001100000011110010000110000111100111100111111001100111'
num_list = []
for i in range(0,len(S),7):
    Bins = S[i:i+7]
    num_list.append(BinToDec(Bins))

print(*num_list)