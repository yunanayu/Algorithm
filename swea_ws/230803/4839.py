# # 이진탐색
# def binarySearch(P, key):
#     start = 1
#     end = P
#     middle = int((start + end) // 2)
#     cnt = 1
#     while P != middle:
#         if middle == key:
#             cnt = 0
#         elif middle > key:
#             end = middle 
#             cnt += 1
#         else:
#             start = middle
#             cnt += 1
#     return cnt
            

# TC = int(input())

# for tc in range(1, TC+1):
#     P, Pa, Pb = map(int, input().split())

#     if binarySearch(P, Pa) > binarySearch(P, Pb):
#         print(f'#{tc} A')
#     elif binarySearch(P, Pa) < binarySearch(P, Pb):
#         print(f'#{tc} B')
#     else:
#         print(f'#{tc} 0')

# def binary_search(page, P):
#     start = 1
#     end = page
#     middle = 0
#     count = 1
#     while P != middle:
#         middle = int((start + end) / 2)
#         if middle > P:
#             end = middle
#         else:
#             start = middle
#         count += 1
#     return count

# T = int(input())
# for tc in range(1, T+1):
#     pages, Pa, Pb = map(int, input().split())
#     A = binary_search(pages, Pa)
#     B = binary_search(pages, Pb)
#     ans = 0
#     if A < B:
#         ans = 'A'
#     elif A > B:
#         ans = 'B'
#     else:
#         ans = 0
#     print(f'#{tc} {ans}')

def Search(all_page, page):
    start = 1
    end = all_page
    # 탐색 수
    result = 0

    while start <= end:
        middle = int((start + end) // 2)
        # 중앙값과 찾는 값이 같으면 return
        if middle == page:
            result += 1
            return result
        # 찾는 값이 중앙값보다 크면 시작값 = 중앙값
        elif middle < page:
            start = middle
            result += 1
        # 찾는 값이 중앙값보다 작으면 마지막값 = 중앙값
        else:
            end = middle
            result += 1

# T :  테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # P : 책의 전체 쪽 수, A : A가 찾을 쪽 번호, B : B가 찾을 쪽 번호
    P, A, B = map(int,input().split())

    # A 탐색수
    a = Search(P,A)
    # B 탐색수
    b = Search(P,B)

    # 탐색수가 더 작은 값이 이김 -> 결과도출
    if a < b:
        print(f'#{tc} A')
    elif b < a:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')