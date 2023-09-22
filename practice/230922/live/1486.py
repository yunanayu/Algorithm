# 장훈이의 높은 선반
def recur(level, acc_height):
    global ans
    # 들어가기 전(가지치기)
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요가 없다!
    if acc_height >= M:
        ans  = min(ans, acc_height)
        return
    # 기저조건
    if level == N:
        return

    # 다음 재귀함수 호출
    # 해당 점원을 탑에 쓸 경우
    recur(level+1, acc_height + arr[level])
    # 안쓸경우
    recur(level+1, acc_height)
    # 돌아왔을 때



T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    recur(0, 0)
    print(f'#{tc}',abs(ans-M))