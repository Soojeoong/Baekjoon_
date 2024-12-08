def check(matrix, x, y, n): # 현재 영역이 모두 같은 값인지 확인하는 함수
    value = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j] != value:
                return False, None
    return True, value

def compress(matrix, x, y, n): # x, y: 현재 영역의 시작 좌표 n: 현재 영역의 크기
    # 현재 영역이 모두 같은 값인지 확인
    homogeneous, value = check(matrix, x, y, n)
    if homogeneous:  # 모두 같다면 해당 값 반환
        return str(value)
    
    # 같지 않다면 4개의 영역으로 나눠서 재귀 호출
    half = n // 2
    top_left = compress(matrix, x, y, half)
    top_right = compress(matrix, x, y + half, half)
    bottom_left = compress(matrix, x + half, y, half)
    bottom_right = compress(matrix, x + half, y + half, half)

    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

    
N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)] 
result = compress(matrix, 0, 0, N)
print(result)