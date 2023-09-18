# 병합정렬

def merge(left, right):
    result = []
    L = len(left)
    R = len(right)
    while L > 0 or R > 0:
        if L > 0 and R > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif L > 0:
            result.append(left.pop(0))
        elif R > 0:
            result.append(right.pop(0))

    return result

# def merge(l, r):
#     result = []
#     lp = rp = 0
#     while lp<len(l) and rp < len(r):
#         if l[lp] < r[rp]:
#             result.append(l[lp])
#             lp += 1
#         else:
#             result.append(r[rp])
#             rp += 1
#         result += l[lp:]
#         result += r[rp:]
#     return result


def merge_sort(lst):
    L = len(lst)

    if L == 1:
        return lst

    left = []
    right = []
    mid = N//2
    # left = lst[:mid]
    # right = lst[mid:]
    #
    for i in lst[:mid]:
        left.append(i)

    for i in lst[mid:]:
        right.append(i)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



T = int(input())

for tc in range(1, T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)
    print(arr)