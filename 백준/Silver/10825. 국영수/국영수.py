# 국영수

N = int(input()) # 반 학생 수
students = []

for i in range(N):
    name, Korean, English, Math = input().split()
    students.append((name, int(Korean), int(English), int(Math)))

# 1. 국어 점수가 내림차순
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로(오름차순)
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 (내림차순)
# 4. 모든  점수가 같으면 이름이 사전 순으로 증가하는 순서로. (아스키코드 - 대문자가 앞으로 오게됨) (오름차순순)

students.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(students[i][0])