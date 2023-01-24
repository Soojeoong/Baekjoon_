from sys import stdin

# 시험장 개수 입력 받기
N = int(stdin.readline())
#  각 시험장의 응시자 수 입력 받기
A = list(map(int, stdin.readline().split()))
# 총감독관이 감시하는 응시자 수, 부감독관 감시 응시자 수 입력 받기
B, C = map(int, stdin.readline().split())
# 감독관 수 합계
spv = 0

for i in range(N):
    if A[i] - B >= 0:
        A[i] -= B
        spv += 1  # 총감독관 수 더하기
        if A[i] % C == 0:
            spv += A[i] // C
        else:
            spv += (A[i] // C) + 1
    else:  # 감독관 수는 최소 1명
        spv += 1

print(spv)