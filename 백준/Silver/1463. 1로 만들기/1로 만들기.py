N = int(input())
d = [0] * (N+1)

for i in range(2, N+1):
    d[i] = d[i-1] + 1 # 1을 빼는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1) # 3으로 나누는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 2로 나누는 경우
    
print(d[N])