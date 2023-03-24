# 1. 마지막 날부터 거꾸로 
# 2. 해당 날짜에 수행할 수 있는 점수 리스트에 넣고
# 3. 그 중 가장 큰 점수 pop해서 더하기

from sys import stdin

# 과제 수 입력
N = int(stdin.readline())
# 과제기한, 점수 입력
project = [list(map(int, stdin.readline().split())) for _ in range(N)]

project.sort() # 오름차순 정렬
canPJ = [] # 해당 일에 가능한 과제 리스트
score = 0

for day in range(N, 0, -1): # 마지막 날부터 거꾸로
    while project and project[-1][0] >= day: # 해당 날 이상의 과제 리스트 중
        canPJ.append(project.pop()[1]) # 점수가 가장 큰 것 pop

    if canPJ:  # 할 수 있는 과제가 있다면
        canPJ.sort() # 가장 큰 점수를 담기 위해
        score += canPJ.pop() # 점수 더하기

print(score)