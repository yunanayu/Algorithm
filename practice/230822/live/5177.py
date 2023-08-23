'''
N+1 개 배열 생성
last = 0
enQ(7)

enq(n)
    last +=1
    h[last] = n    => 완전 이진 트리 유지
                    => 부모 < 자식
    while 부모가 있을 때, p>0 and h[p] > h[c] # 최소합에 의해           부모가 있을때
            h[p] <-> h[c]       부모 > 자식
            c <-p            -> 부모 자식 교환
            p<- c//2
'''