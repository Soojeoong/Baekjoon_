from sys import stdin

# 물품의 수, 버틸 수 있는 무게 입력
N, K = map(int, stdin.readline().split())

# 이차원 배열 초기화
W_V = [(0, 0)]
dp = [[0] * (K+1) for _ in range(N+1)]

# 물건의 무게, 물건의 가치 입력
for _ in range(N):
    W_V.append(list(map(int, stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        # W와 V 분리
        W = W_V[i][0]
        V = W_V[i][1]

        # 버틸 수 있는 무게 < 물건의 무게
        if j < W:
            dp[i][j] = dp[i-1][j]  # 이전  값에 넣기
        # 버틸 수 있는 무게 > 물건의 무게
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V) # 이전 값과 비교해 큰 값 넣기

print(dp[N][K])