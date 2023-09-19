# lst를 정렬 한 수 결과를 return

def merge(l, r):
    global cnt
    result = []
    lp = rp = 0
    while lp<len(l) and rp < len(r):
        if l[lp] < r[rp]:
            result.append(l[lp])
            lp += 1
        else:
            result.append(r[rp])
            rp += 1
    if l[-1] > r[-1] :
        cnt += 1
    result += l[lp:]
    result += r[rp:]
    return result

def merge_sort(lst):
    N = len(lst)
    if N == 1:
        return lst
    m = N//2
    left_lst = merge_sort(lst[:m])
    right_lst = merge_sort(lst[m:])

    result = merge(left_lst, right_lst)
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc}', result[N//2], cnt)