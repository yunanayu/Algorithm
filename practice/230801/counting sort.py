# 카운팅 정렬

data = [0, 4, 1, 3, 1, 2, 4, 1]
# 0, 1, 1, 1, 2, 3, 4, 4

# i 번째 index에 i가 나온 횟수를 저장+
N = len(data)
counts = [0] * 10
for d in data:
    counts[d] += 1 # counts[d] = counts[d] + 1

print(counts)

for i in range(9):
    counts[i+1] = counts[i] + counts[i + 1]
print(counts)

result = [-1] * N
for d in data:
    position = counts[d] - 1
    result[position] = d
    counts[d] -= 1

print(result)