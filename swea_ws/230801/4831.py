TC = int(input())

def bus_char(K,N,M,stops):
    for k in range(K):

    return



for tc in range(1,TC+1):
    K, N, M = map(int, input().split())
    stops = [0] + list(map(int, input().split())) + [N] # 리스트 합산
    print(stops)
















#
# def check():
#     #stops의 간격이 k 보다 크면 결과가 0
#     for st in range(M+1):
#         if stops[st+1] - stops[st] > k:
#             return 0
#      last_stop = 0
#       for s in range(1,M+2): #stop의 데이터가 아닌 인덱스 값이 필요하기 때문에 range 사용
#           if laststop + K < stops[s]:
    #            laststop = stops[s-1]
                #cnt += 1
    #
    #
    #        if laststop + K >= stops[s]
    #        laststop = stops[s-1]
#            continue
#           else:
#
                cnt += 1
#
#
# TC = int(input())
#
# for tc in range(1,TC+1):
#     K, N, M = map(int(input()))
#     stops = [0] + list(map(int, input().split())) + [N]
#     ..

