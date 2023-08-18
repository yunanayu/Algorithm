A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A == B or B == C:
    print(1000 + 100 * A)
elif C == A:
    print(1000 + 100 * A)
else:
    if A > B and A > C:
        print(A * 100)
    elif B > A and B > C:
        print(B * 100)
    else:
        print(C * 100)