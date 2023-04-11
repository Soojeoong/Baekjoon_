# 동전 개수 최솟값 구하기
# 동전 총류 N개
# 가치의 합 K
# 동전의 가치 A

from sys import stdin
input = stdin.readline
N, K = map(int, input().split())

A = [int(input()) for i in range(N)]
A.sort(reverse=True) # 내림차순 정렬

count = 0

for a in A:
    count += K // a
    K %= a

print(count)