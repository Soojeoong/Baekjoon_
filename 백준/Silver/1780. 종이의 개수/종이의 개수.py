def check(paper, x, y, n): # paper : 종이 행렬, x, y : 시작 좌표, n : 현재 영역의 크기
    value = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != value:
                return False
    return True

def solve(paper, x, y, n): # paper : 종이 행렬, x, y : 시작 좌표, n : 현재 영역의 크기
    if check(paper, x, y, n):  # 모두 같은 숫자라면 개수 반환
        value = paper[x][y]
        if value == -1:
            return (1, 0, 0)  # -1 개수
        elif value == 0:
            return (0, 1, 0)  # 0 개수
        elif value == 1:
            return (0, 0, 1)  # 1 개수

    # 9등분 후 재귀적으로 호출
    size = n // 3
    count_minus1, count_0, count_1 = 0, 0, 0

    for i in range(3):
        for j in range(3):
            sub_result = solve(paper, x + i * size, y + j * size, size)
            count_minus1 += sub_result[0]
            count_0 += sub_result[1]
            count_1 += sub_result[2]

    return (count_minus1, count_0, count_1)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산
result_minus1, result_0, result_1 = solve(paper, 0, 0, N)

# 출력
print(result_minus1)
print(result_0)
print(result_1)
