result = []
N, K = map(int, input().split())
for n in range(1, N+1):
    value = N%n
    if value != 0:
        result.append(N%n)
result.sort()
if len(result) >= K:
    print(result[K-1])
else:
    print(0)