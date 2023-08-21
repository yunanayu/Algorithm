N = 13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
G = [[0] for _ in range(N + 1)]

for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    G[p].append(c)
print(G)

def post_order(root):
    if len(G[root]) >= 1:
        post_order(G[root][0])      # 그래프에 데이터가 비어있을 때 혹은 1개만 존재할때를 생각해줘야함 -> 길이로 파악
    if len(G[root]) == 2:
        post_order(G[root][1])
    print(root)


post_order(1)