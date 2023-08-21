def print_tree(root):
    if cl[root]:    #왼쪽이 tree 이면:
        print_tree(cl[root])    #(root의 왼쪽서브트리의 root)
    print(root)
    if cr[root]:    #오른쪽이 tree이면:
        print_tree(cr[root])    #(root의 오른쪽서브트리의 root)


def print_tree2(root):
    if root:
        print_tree(cl[root])
        print(root)
        print_tree(cr[root])


N =13
s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
lst = list(map(int, s.split()))
G = [[0] for _ in range(N+1)]
cl = [0] * (N+1)
cr = [0] * (N+1)
pn = [0] * (N+1)  # 부모 정보 저장
for i in range(0, len(lst), 2):
    p = lst[i]
    c = lst[i+1]
    pn[c] = p
    if cl[p] == 0:
        cl[p] = c
    else:
        cr[p] = c

print_tree(1)