N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
d = [0] * (N+1)

d[1] = stairs[1]
if N > 1:
    d[2] = stairs[1] + stairs[2]

for i in range(3, N+1):
    d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])
    
    
print(d[N])