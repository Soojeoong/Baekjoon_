# 바구니 뒤집기

# N개 바구니, M번 바구니의 순서를 역순으로 
# 범위 정하고, 그 안의 바구니의 순서를 역순으로


N, M = map(int, input().split())
nlist = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    nlist[i-1:j] = nlist[i-1:j][::-1]  # 역순 교환환
    
print(*nlist) # 공백으로 구분해 출력력
