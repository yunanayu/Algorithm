# 최대힙으로 사용하고 싶으면 데이터에 -를 붙여서 넣고 뺄 때 -를 다시 붙여서 나오면 됨

import heapq

heap = []            # creates an empty heap
heapq.heappush(heap, 10) # pushes a new item on the heap
heapq.heappush(heap, 20)
heapq.heappush(heap, 30)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3) ## 3 있을때 없을 때 구분해보기
print(heap)

item = heapq.heappop(heap) # pops the smallest item from the heap
print(heap)