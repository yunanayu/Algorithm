total = 20
Q = []
h = 1
sum_V = 0
while sum_V < total:
    print(Q)
    # 처음 줄 서는 사람
    Q.append((h, 1))
    h += 1

    # 받아가는 사람
    new_h, candy = Q.pop(0)
    print(f'{new_h}가 {candy} 받아감')
    sum_V += candy


    # 받은사람이 다시 줄서기
    Q.append((h, candy+1))

print(f'{new_h} 가 마지막')