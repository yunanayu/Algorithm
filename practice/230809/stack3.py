s = 'CAAABBA'
ST = []

for c in s:
    if not ST:
        스택에 넣는다.
    elif ST[-1] == c: # 같으면 스택의 데이터 pop
        스택의 데이터 pop
    else:
        스택에 넣는다.

for c in s:
    if not ST or ST[-1] != c:
        스택에 넣는다
    else:
        스택의 데이터 pop
