from sys import stdin

N = int(stdin.readline())
cnt = 0 # 3kg, 5kg 봉지 수를 합친 전체 봉지 수

while N >= 0:
    if N % 5 == 0:
        cnt += (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)