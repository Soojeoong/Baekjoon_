# https://www.acmicpc.net/problem/1309
from sys import stdin

N = int(stdin.readline())
# N=0 : 1개
# N=1 : 3개
# N번째 : 3*빈 우리 + 2*사자있는우리
# zoo[i] = (3*zoo[i-2] + 2*(zoo[i-1]-zoo[i-2]))
zoo = [1,3] + [0]*(N-1)
for i in range(2, N+1):
    zoo[i] = zoo[i-2] + 2*zoo[i-1]
    zoo[i] %= 9901
print(zoo[N])