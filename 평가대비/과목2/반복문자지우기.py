TC = int(input())
for tc in range(1, TC+1):
    txt = list(input())
    ST = []
    for t in txt:
        if not ST or ST[-1] != t:
            ST.append(t)
        else:
            ST.pop()

    print(len(ST))
