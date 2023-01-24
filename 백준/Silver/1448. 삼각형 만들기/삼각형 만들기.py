# https://www.acmicpc.net/problem/1448
from sys import stdin

# 빨대의 개수 입력받기
n = int(stdin.readline())
A = []
# 빨대 크기 입력받기
for _ in range(n):
    A.append(int(stdin.readline()))
# 내림차순 정렬
A.sort(reverse=True)

max = -1
for i in range(n-2):
    # 삼각형 조건 : 두변의 길이 합 > 가장 긴 변
    if (A[i+1]+A[i+2]) > A[i]:
        max = A[i]+A[i+1]+A[i+2]
        break # 삼각형이 된다 -> 길이합이 최대인 삼각형 완성

# 삼각형 세 변의 길이의 합의 최댓값 출력
print(max)

