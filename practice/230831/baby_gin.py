# 베이비진이면  True / 아니면 False
def isBabygin(cnts):
    for i in range(10):
        if cnts[i] >= 3:
            return True
        if cnts[i] >= 1 and cnts[i+1]>=1 and cnts[i+2]>=1:  # out of range 방지를 위히ㅐ 배열 12개 만듬 or 반복문 두개로 쪼개기
            return True
    return False


def isBabygin2(cnts):
    tri = 0
    run = 0
    i = 0
    while i < 10:
        if cnts[i] >= 3:
            cnts[i] -= 3
            tri += 1
            continue
        if cnts[i] >= 1 and cnts[i+1]>=1 and cnts[i+2]>=1:
            cnts[i] -= 1
            cnts[i+1] -= 1
            cnts[i+2] -= 1
            run += 1
            continue
        i += 1
    if tri + run == 2:
        return True
    return False


TC = int(input())
for tc in range(1, TC+1):
    lst = list(map(int, input().split()))

    cnt_1 = [0] * 13 # out of range
    cnt_2 = [0] * 13
    winner = 0

    for i in range(0, 12, 2):
        n1 = lst[i]
        n2 = lst[i+1]
        cnt_1[n1] += 1
        cnt_2[n2] += 1

        if isBabygin(cnt_1):
            winner = 1
            break

        if isBabygin(cnt_2):
            winner = 2
            break

print(winner)