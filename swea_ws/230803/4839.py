# 이진탐색
def binarySearch(p, key):
    start = 1
    end = p
    cnt = 1
    while start < end:
        middle = int((start + end) // 2)
        if middle == key:
            break
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt


TC = int(input())

for tc in range(1, TC+1):
    P, Pa, Pb = map(int, input().split())

    if binarySearch(P, Pa) > binarySearch(P, Pb):
        print(f'#{tc} B')
    elif binarySearch(P, Pa) < binarySearch(P, Pb):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')


# # 이진 검색
# def bi_search(p, goals):
#     l = 1  # 시작 페이지
#     r = p  # 최종 페이지
#     c = 0  # 중간 페이지 지점을 시작지점으로 초기화 해야하니까 0
#     while l <= p:  # 시작 페이지부터 최종 페이지 까지 돌면서
#         middle = int((l + r) // 2)  # // 중간 지점값을 몫만 꺼내서
#         if middle == goals:  # 중간 페이지가 목표 지점과 같다면
#             return c  # 그대로 리턴
#         elif middle < goals:  # 중간 페이지가 목표 지점보다 작다면
#             l = middle  # 중간 페이지를 시작 페이지로 변경하고
#             c += 1  # 중간 페이지를 하나씩 늘려 목표 지점을 찾아라
#         elif middle > goals:  # 중간 페이지가 목표 지점보다 크다면
#             r = middle  # 중간 페이지를 최종 페이지로 변경하고
#             c += 1  # 중간 페이지를 하나씩 늘려 목표 지점을 찾아라
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     P, Pa, Pb = map(int, input().split())  # 각각 하나씩 분배 list x
#
#     goalA = bi_search(P, Pa)  # 각각 함수 호출 하고 인자들 할당
#     goalB = bi_search(P, Pb)
#
#     if goalA < goalB:  # 값이 적은게 목표 지점까지 빨리 찾은거니까
#         result = 'A'  # 값이 적은게 승리
#     elif goalA > goalB:
#         result = 'B'
#     else:  # 무승부는 0
#         result = 0
#
#     print(f'#{tc} {result}')
