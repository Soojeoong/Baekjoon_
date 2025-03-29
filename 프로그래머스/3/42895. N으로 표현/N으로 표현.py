    # DP # 최솟값
    # N 개수 2부터 시작해서 8까지?
    #             N
    #            / |
    # NN, N+N, N*N, N/N, N-N, (사칙연산)?
    # 이렇게 재귀?하면서 number이 되면 N min 개수 반환
def solution(N, number):
    if N == number:  # N을 1번 사용하여 목표를 달성할 수 있는 경우
        return 1

    # dp[i]는 N을 i번 사용해서 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # i번 반복되는 N으로 이루어진 수 추가 (예: 5, 55, 555, ...)
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for op1 in dp[j]: # op1 : 숫자
                for op2 in dp[i - j]: # op2 : 숫자
                    dp[i].add(op1 + op2)  # 덧셈
                    dp[i].add(op1 - op2)  # 뺄셈
                    dp[i].add(op1 * op2)  # 곱셈
                    if op2 != 0:  # 나눗셈은 0으로 나누지 않도록 주의
                        dp[i].add(op1 // op2)

        if number in dp[i]:  # 목표 숫자가 포함된 경우
            return i

    return -1  # 8번 이하로 표현할 수 없는 경우


# 테스트 예제
print(solution(5, 12))  # 출력: 4
print(solution(2, 11))  # 출력: 3
