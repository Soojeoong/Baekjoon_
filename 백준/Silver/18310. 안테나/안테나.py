# 안테나

N = int(input()) # 집의 수 N

houses = list(map(int, input().split()))

houses.sort()

# 중앙값 O(1)
result = houses[(N-1)//2]
print(result)