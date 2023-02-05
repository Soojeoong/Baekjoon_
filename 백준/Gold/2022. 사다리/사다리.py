# https://www.acmicpc.net/problem/2022
from sys import stdin

def f(x, y, w):
    h1 = (x**2 - w**2)**0.5
    h2 = (y**2 - w**2)**0.5
    c = (h1*h2)/(h1+h2)
    return c

x, y, c = map(float, stdin.readline().split())
start, end = 1, min(x,y)
result = 0

while end-start >= 0.000001:
    #이진 탐색
    mid = (start+end)/2
    if f(x, y, mid) >= c:
        result = mid
        start = mid
    else:
        end = mid
# print(round(result, 3))
# print(format(result, ".3f"))
print(f'{result:.3f}')
