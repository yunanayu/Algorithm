# 이진검색 - 반복문

arr = [2, 4, 7, 9, 11, 19, 23]

# 이진검색은 반드시 정렬된 데이터로 수행하기

arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) - 1

    # low > high 라면 데이터를 못찾은 경우임
    while low <= high:
        mid = (low+high)// 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은경우
        elif arr[mid] < target:
            low = mid + 1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1

    return "해당 데이터는 없습니다."


print(f'9 => {binarySearch(9)}')
print(f'4 => {binarySearch(4)}')
print(f'1 => {binarySearch(1)}')

