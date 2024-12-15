# N-Queen
# https://www.acmicpc.net/problem/9663

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0: 
            v1[j] = v2[n+j] = v3[n-j] = 1 # 방문 표시
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0 # 방문 해제

N = int(input())
ans = 0
v1 = [0]*N
v2 = [0]*(2*N) # 우상향 대각선  # 합이 같음 
v3 = [0]*(2*N) # 우하향 대각선  # 차가 같음
dfs(0)
print(ans)